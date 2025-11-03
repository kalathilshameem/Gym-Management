from django.urls import path
from . import views
from .views import index,about

urlpatterns = [
    path('', index, name='index'),
    path('', about,name='about'),
    path('contact/', contact, name='contact'),
    path('contact-view/', contact_view, name='contact'),
    path('contact-submissions/', views.contact_list, name='contact_list'),
]
