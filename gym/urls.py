from django.urls import path
from . import views
from .views import index,about

urlpatterns = [
    path('', index, name='index'),
    path('', about,name='about')
]
