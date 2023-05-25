from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, View, UpdateView, ListView

from course.models import Course, Comment
from .forms import UserCreationForm, LoginForm, MyPasswordResetForm, MyPasswordConfirmForm, UserChangeForm
from .models import MyUser
from django.shortcuts import redirect, render, get_object_or_404


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


class LoginView(FormView):
    template_name = 'account/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if self.request.POST.get('remember'):
            self.request.session.set_expiry(1209600)  # 2 weeks
        else:
            self.request.session.set_expiry(0)  # session expires when browser closes
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class MyPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset_form.html'
    form_class = MyPasswordResetForm
    success_url = reverse_lazy("account:password_reset_done")


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'account/password_reset_confirm.html'
    form_class = MyPasswordConfirmForm
    success_url = reverse_lazy('account:password_reset_complete')


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'account/password_reset_complete.html'


class UserPanelView(View):
    def get(self, request, username):
        if request.user.username != username:
            return redirect('account:user_panel', request.user.username)
        user = MyUser.objects.get(username=username)
        user_courses = user.student_courses.all().count()
        courses = Course.objects.all().count()

        return render(request, 'account/profile.html', {'user': user, 'courses':courses, 'user_courses':user_courses})

class UserUpdatingView(UpdateView):
    template_name = 'account/profile_update.html'
    form_class = UserChangeForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('account:user_panel', kwargs={'username':self.kwargs.get('username')})

    def get_object(self, queryset=None):
        queryset = MyUser.objects.get(username=self.kwargs.get('username'))
        return queryset



class UserCoursesView(ListView):
    template_name = 'account/profile_course.html'
    model = Course
    context_object_name = 'courses'
    paginate_by = 1
    def get_queryset(self):
        queryset = super(UserCoursesView, self).get_queryset()
        queryset = Course.objects.all().filter(student=self.request.user.id)
        return queryset

class UserCommentsView(ListView):
    template_name = 'account/profile_comments.html'
    model = Comment
    context_object_name = 'comments'
    paginate_by = 1
    def get_queryset(self):
        queryset = super(UserCommentsView, self).get_queryset()
        queryset = Comment.objects.all().filter(email=self.request.user.email)
        return queryset

def delete_comment(request,username, id):
    comment = get_object_or_404(Comment, id=id)
    comment.delete()
    return redirect('account:user_panel_comments', username)

def logout_view(request):
    logout(request)
    return redirect('home')
