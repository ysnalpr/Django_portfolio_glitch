from django.forms import ModelForm, fields

from .models import Message


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']

