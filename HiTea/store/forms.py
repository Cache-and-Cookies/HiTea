from django import forms
from .models import Message

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Message
        fields = [
            'first_name',
            'last_name',
            'email',
            'message',
        ]

