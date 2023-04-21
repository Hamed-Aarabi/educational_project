from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import UserCreationForm
from .models import MyUser
from django.shortcuts import redirect


class SignUpView(FormView):
    template_name = 'account/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        cd = form.cleaned_data
        if self.request.POST.get('check'):
            MyUser.objects.create_user(phone=cd['phone'], email=cd['email'], username=cd['username'],
                                       password=cd['password2'])
        else:
            messages.error(self.request, 'برای ثبت نام قوانین و مقررارت را مطالعه و بپذیرید.')
            return redirect('account:signup')
        return super(SignUpView, self).form_valid(form)
