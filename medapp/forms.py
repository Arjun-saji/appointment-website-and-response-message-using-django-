from django import forms
from .models import *

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'service', 'appointment_date', 'email', 'phone', 'notes']
        
        widgets = {
            'patient_name': forms.TextInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'Enter your name',
                'onfocus': 'this.placeholder = \'\'',
                'onblur': 'this.placeholder = \'Enter your name\''
            }),
            'service': forms.Select(attrs={
                'class': 'form-control valid',
                'onfocus': 'this.placeholder = \'\'',
                'onblur': 'this.placeholder = \'Services\''
            }),
            'appointment_date': forms.DateTimeInput(attrs={
                'class': 'form-control valid',
                'type': 'date',
                'onfocus': 'this.placeholder = \'\'',
                'onblur': 'this.placeholder = \'Appointment Date\''
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'Email',
                'onfocus': 'this.placeholder = \'\'',
                'onblur': 'this.placeholder = \'Enter email address\''
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'Phone No.',
                'onfocus': 'this.placeholder = \'\'',
                'onblur': 'this.placeholder = \'Phone No.\''
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'cols': 30,
                'rows': 9,
                'placeholder': 'Enter Message',
                'onfocus': 'this.placeholder = \'\'',
                'onblur': 'this.placeholder = \'Enter Message\''
            }),
        }
