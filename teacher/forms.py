from django import forms
from .models import *


class TeachRequestForm(forms.ModelForm):
    class Meta:
        model = TeachRequest
        fields = '__all__'

        widgets = {
            'fullname': forms.TextInput(
                attrs={'type': "text", 'class': "form-control form-control-lg", 'placeholder': "نام و نام خانوادگی"}),
            'email': forms.EmailInput(
                attrs={'type': "email", 'class': "form-control form-control-lg", 'placeholder': "ایمیل"}),
            'phone': forms.TextInput(
                attrs={'type': "tel", 'class': "form-control form-control-lg", 'placeholder': "شماره تلفن"}),
            'field': forms.TextInput(
                attrs={'type': "text", 'class': "form-control form-control-lg", 'placeholder': "عنوان آموزش"}),
            'description': forms.Textarea(attrs={'rows': "5", 'class': "form-control", 'placeholder': "توضیحات"}),

        }
