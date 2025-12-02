from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class ContactForm(models.Model):
    name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

@property
def bmi(self):
    return round(float(self.weight) / (float(self.height) ** 2), 2)

@property
def days_remaining(self):
    return (self.membership_end - datetime.today().date()).days


def _str_(self):
    return f"{self.user.get_full_name()} ({self.biometric_id})"


class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def _str_(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Remove null=True
    email = models.EmailField(unique=True)
    biometric_id = models.CharField(max_length=100, unique=True)
    height = models.DecimalField(max_digits=4, decimal_places=2)  # Allows values like 1.75m
    weight = models.FloatField()
    membership_start = models.DateField()
    membership_end = models.DateField()
    emergency_contact = models.CharField(max_length=15)
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

