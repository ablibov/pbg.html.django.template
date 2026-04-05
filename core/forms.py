from django import forms
from core.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'message', 'avatar']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Last name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', "placeholder": "Email"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', "placeholder": "Phone"}),
            'message': forms.Textarea(attrs={'class': 'form-control', "placeholder": "Message", 'style': 'height:125px;',}),
            'avatar': forms.FileInput(attrs={'class': 'form-control', "placeholder": "Avatar"}),
        }