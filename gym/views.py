import datetime
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import ContactForm
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
