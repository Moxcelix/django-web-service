from django import forms
from app.models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'phone_number', 'address']