from django.forms import forms
from django.forms import ModelForm
from .models import Task


class RegisterForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'