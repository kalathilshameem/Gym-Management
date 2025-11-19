import datetime
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError
from gym.forms import MemberForm
from .models import ContactForm, Member
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')


def contact(request):
    return render(request, 'contact.html')
        
def dashboard(request):
    return render(request, 'dashboard.html')
    
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        contact_no = request.POST.get("contact_no")
        email = request.POST.get("email")
        message = request.POST.get("message")
        contact = ContactForm(name=name, contact_no=contact_no, email=email, message=message)
        contact.save()

        messages.success(request, "Your message has been sent successfully!")
        return redirect("contact")

    return render(request, "contact.html")

def contact_list(request):
    contacts = ContactForm.objects.all().order_by('-created_at')
    return render(request, 'contact_list.html', {'contacts': contacts})

def services(request):
    return render(request, 'services.html')

def member_registration(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            try:
                # Create User first
                user = User.objects.create_user(
                    username=form.cleaned_data['biometric_id'],
                    email=form.cleaned_data['email'],
                    password='default_password@123'  
                )

                # Create Member with the user reference
                member = form.save(commit=False)
                member.user = user
                member.save()

                messages.success(request, 'Member registered successfully!')
                return redirect('members_list')

            except IntegrityError as e:
                messages.error(request, f'Database error: {str(e)}')
            except Exception as e:
                messages.error(request, f'Unexpected error: {str(e)}')
        else:
            messages.error(request, 'Please correct the errors below')
    else:
        form = MemberForm()

    return render(request, 'member_registration.html', {'form': form})

def members_list(request):
    today = timezone.now().date()
    members = Member.objects.all().order_by('-id')

    for member in members:
        member.days_remaining = (member.membership_end - today).days
        member.bmi = round(float(member.weight) / (float(member.height) ** 2), 1)

    return render(request, 'members_list.html', {'members': members})


def edit_member(request, id):
    member = get_object_or_404(Member, id=id)
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member updated successfully!')
            return redirect('members_list')
    else:
        form = MemberForm(instance=member)

    return render(request, 'edit_member.html', {'form': form})

def delete_member(request, member_id):  # Parameter name matches URL pattern
    if request.method == 'POST':
        member = get_object_or_404(Member, id=member_id)
        try:
            user = member.user
            user.delete()
            messages.success(request, f'Member {member.name} deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting member: {str(e)}')
        return redirect('members_list')
    return HttpResponseNotAllowed(['POST'])


def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Member added successfully!')
            return redirect('members_list')
    else:
        form = MemberForm()

    return render(request, 'edit_member.html', {'form': form})

