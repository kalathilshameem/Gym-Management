from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    return render(request, 'index.html')
