from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import MyUser
from django.contrib.auth.views import PasswordResetForm, SetPasswordForm


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'type': 'password', 'placeholder': 'رمز عبور'}))
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'type': 'password', 'placeholder': 'تکرار رمز عبور'})
    )

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'phone']

        widgets = {
            'username': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'نام کاربری', 'type': 'text'}),
            'email': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'ایمیل', 'type': 'email'}),
            'phone': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'placeholder': 'شماره تلفن', 'type': 'tel'}),
        }

    def clean(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        if MyUser.objects.filter(username=username).exists():
            raise ValidationError('نام کاربری قبلا ثبت نام شده است.', code='username_exist')
        if MyUser.objects.filter(email=email).exists():
            raise ValidationError('ایمیل قبلا ثبت نام شده است.', code='email_exist')
        if MyUser.objects.filter(phone=phone).exists():
            raise ValidationError('شماره تلفن قبلا ثبت نام شده است.', code='phone_exist')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("گذرواژه ها مشابه نیستند", code='password_match')
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """

    # password = ReadOnlyPasswordHashField()
    SEX_CHOICES = (
        ('man', 'مرد'),
        ('woman', 'زن'),
        ('other', 'دیگر'),
    )

    sex = forms.ChoiceField(choices=SEX_CHOICES)
    class Meta:
        model = MyUser
        fields = ('email', 'username', 'first_name', 'last_name', 'image', 'phone', 'sex')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg', 'id': 'email', 'type': 'email'}),
            'username': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'id': 'username', 'type': 'text'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'id': 'name', 'type': 'text'}),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control form-control-lg', 'id': 'lastname', 'type': 'text'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg', 'id': 'avatar', 'type': 'file'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'phone', 'type': 'tel'}),
             # 'sex': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'sex'}),

        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'type': 'text', 'placeholder': 'نام کاربری'}))
    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'type': 'password', 'placeholder': 'رمز عبور'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if authenticate(username=username, password=password) is None:
            raise ValidationError('نام کاربری یا رمز عبور اشتباه می باشد.', code='invalid_login')


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'ایمیل', 'type': 'email'}))

    def clean(self):
        email = self.cleaned_data.get('email')
        if not MyUser.objects.filter(email=email).exists():
            raise ValidationError('کاربری با ایمیل وارد شده یافت نشد.', code='email_not_found')


class MyPasswordConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label="Password", widget=forms.PasswordInput(
        attrs={'class': 'form-control form-control-lg', 'type': 'password', 'placeholder': 'رمز عبور'}))
    new_password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'type': 'password', 'placeholder': 'تکرار رمز عبور'})
    )

    def clean_new_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("گذرواژه ها مشابه نیستند", code='password_reset_match')
        return password2
