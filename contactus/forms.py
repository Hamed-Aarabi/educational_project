from django import forms
from .models import Contactus




class ContactusForm(forms.ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'

        widgets = {
            'full_name':forms.TextInput(attrs={'type':"text", 'class':"form-control form-control-lg", 'placeholder':"نام و نام خانوادگی"}),
            'email':forms.EmailInput(attrs={'type':"text", 'class':"form-control form-control-lg", 'placeholder':"ایمیل"}),
            'subject':forms.TextInput(attrs={'type':"text", 'class':"form-control form-control-lg", 'placeholder':"عنوان"}),
            'text':forms.Textarea(attrs={'rows':"5", 'class':"form-control", 'placeholder':"متن پیام"}),
        }