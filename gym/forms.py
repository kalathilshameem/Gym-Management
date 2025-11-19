from django.contrib.auth.models import User

from .models import ContactForm
from django import forms
from .models import Member


from django import forms

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['user', 'trainer']
        widgets = {
            'membership_start': forms.DateInput(attrs={'type': 'date'}),
            'membership_end': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # Editing existing instance
            self.fields['biometric_id'].disabled = True

