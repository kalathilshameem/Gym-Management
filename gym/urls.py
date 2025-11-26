from django.urls import path
from . import views
from .views import contact, contact_view, index,about, services, bmi_calculator, bmi_calculator_user

urlpatterns = [
    path('', index, name='index'),
    path('about', about,name='about'),
    path('contact/', contact, name='contact'),
    path('contact-view/', contact_view, name='contact'),
    path('contact-submissions/', views.contact_list, name='contact_list'),
    path('services/', services, name='services'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.member_registration, name='member_registration'),
    path('members/', views.members_list, name='members_list'),
    path('members/add/', views.add_member, name='add_member'),
    path('members/edit/<int:id>/', views.edit_member, name='edit_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),
    path('trainers/', views.manage_trainers, name='trainers_list'),
    path('trainers/edit/<int:id>/', views.edit_trainer, name='edit_trainer'),
    path('trainers/delete/<int:id>/', views.delete_trainer, name='delete_trainer'),
    path('trainers/assign/<int:id>/', views.assign_trainer, name='assign_trainer'),
    path('user/bmi-calculator/', bmi_calculator_user, name='bmi_calculator_user'),
    path('bmi-calculator/', bmi_calculator, name='bmi_calculator')
]
