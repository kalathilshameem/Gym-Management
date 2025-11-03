from django.urls import path
from . import views
from .views import contact, contact_view, index,about, services

urlpatterns = [
    path('', index, name='index'),
    path('about', about,name='about'),
    path('contact/', contact, name='contact'),
    path('contact-view/', contact_view, name='contact'),
    path('contact-submissions/', views.contact_list, name='contact_list'),
    path('services/', services, name='services'),
    path('dashboard/', views.dashboard, name='dashboard')
]
