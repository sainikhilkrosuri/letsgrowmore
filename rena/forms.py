from django import forms
from django.forms import ModelForm
from .models import SubmitForm


class MainForm(ModelForm):
    class Meta:
        model = SubmitForm
        fields = ("name", "pin", "ms", "ds", "java")

        labels = {
            "name": "",
            "pin": "",
            "ms": "MS",
            "ds": "DS",
            "java": "JAVA"
        }

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Name", "width": "100px;"}),
            "pin": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Pin"}),
            "ms": forms.TextInput(attrs={"class": "form-control", "placeholder": "Grade"}),
            "ds": forms.TextInput(attrs={"class": "form-control", "placeholder": "Grade"}),
            "java": forms.TextInput(attrs={"class": "form-control", "placeholder": "Grade"}),
        }
