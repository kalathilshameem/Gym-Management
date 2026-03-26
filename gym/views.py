import datetime
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError
from gym.forms import MemberForm, TrainerForm
from .models import ContactForm, Member, Trainer
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from gym.workouts import generate_workout


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about-us.html')

def bmi_calculator_user(request):
    return render(request, 'bmi_calculator_user.html')

def bmi_calculator(request):
    return render(request, 'bmi_calculator.html')
    
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

def contact_list(request):
    contacts = ContactForm.objects.all().order_by('-created_at')
    return render(request, 'contact_list.html', {'contacts': contacts})


def manage_trainers(request):
    # Handle form submission
    if request.method == 'POST':
        # Check which form was submitted
        if 'add_trainer' in request.POST:
            form = TrainerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Trainer added successfully!')
                return redirect('trainers_list')
        elif 'assign_trainer' in request.POST:
            trainer_id = request.POST.get('trainer_id')
            trainer = get_object_or_404(Trainer, id=trainer_id)
            members = request.POST.getlist('members')
            trainer.member_set.clear()
            for member_id in members:
                member = Member.objects.get(id=member_id)
                member.trainer = trainer
                member.save()
            messages.success(request, 'Assignments updated successfully!')
            return redirect('trainers_list')

    # GET request or invalid form
    trainers = Trainer.objects.prefetch_related('member_set').all()
    members = Member.objects.all()
    form = TrainerForm()  # Empty form for adding new trainers

    return render(request, 'trainers_list.html', {
        'trainers': trainers,
        'members': members,
        'form': form
    })


def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trainer updated successfully!')
            return redirect('trainers_list')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainers.html', {'form': form})


def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        trainer.delete()
        messages.success(request, 'Trainer deleted successfully!')
    return redirect('trainers_list')

def assign_trainer(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        members = request.POST.getlist('members')
        trainer.member_set.clear()
        for member_id in members:
            member = Member.objects.get(id=member_id)
            member.trainer = trainer
            member.save()
        messages.success(request, 'Assignments updated successfully!')
    return redirect('trainers_list')

def bmi_calculator_user(request):
    return render(request, 'bmi_calculator_user.html')

def bmi_calculator(request):
    return render(request, 'bmi_calculator.html')

def workout_planner_user(request):
    workout = None
    
    if request.method == 'POST':
        goal = request.POST.get('goal')
        # Pass the goal to generate_workout
        workout = generate_workout(goal)
    
    return render(request, 'workout_user.html', {'workout': workout})
def workout_planner(request):
    workout = None
    if request.method == 'POST':
        goal = request.POST.get('goal')
        workout = generate_workout(goal)
    return render(request, 'workout_form.html', {'workout': workout})

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())


def admin_logout(request):
    logout(request)
    return redirect('index')
