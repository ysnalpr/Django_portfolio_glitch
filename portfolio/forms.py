from django.forms import ModelForm, widgets
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

from .models import Message


class MessageForm(ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message', 'captcha']

