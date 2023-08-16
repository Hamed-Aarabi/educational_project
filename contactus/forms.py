from django import forms
from .models import *


class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'

        widgets = {
            'full_name': forms.TextInput(
                attrs={'type': "text", 'class': "form-control form-control-lg", 'placeholder': "نام و نام خانوادگی"}),
            'email': forms.EmailInput(
                attrs={'type': "text", 'class': "form-control form-control-lg", 'placeholder': "ایمیل"}),
            'subject': forms.TextInput(
                attrs={'type': "text", 'class': "form-control form-control-lg", 'placeholder': "عنوان"}),
            'text': forms.Textarea(attrs={'rows': "5", 'class': "form-control", 'placeholder': "متن پیام"}),
        }


class CounselForm(forms.ModelForm):
    class Meta:
        model = Counsel
        fields = '__all__'

        widgets = {
            'fullname': forms.TextInput(
                attrs={'type': 'text', 'class': "form-control form-control-lg", 'placeholder': 'نام و نام خانوادگی'}),
            'email': forms.EmailInput(
                attrs={'type': 'email', 'class': "form-control form-control-lg", 'placeholder': 'ایمیل'}),
            'phone': forms.TextInput(
                attrs={'type': 'tel', 'class': "form-control form-control-lg", 'placeholder': 'شماره تلفن'})
        }
