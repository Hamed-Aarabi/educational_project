from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import reverse_lazy
from django.views.generic import FormView, View, ListView
from blog.models import *
from course.models import *
from .forms import *
from .models import MyUser, Ticket
from django.shortcuts import redirect, render, get_object_or_404
from notification.models import *


class SignUpView(FormView):
    template_name = 'account/sign_up.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('account:login')

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
        notify = Notification.objects.all().order_by('-created_at')[:3]
        return render(request, 'account/profile.html',
                      {'user': user, 'courses': courses, 'user_courses': user_courses, 'notify': notify})


def user_update_view(request, username):
    user = MyUser.objects.get(username=username)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('account:user_panel', username)
    else:
        form = UserChangeForm(instance=user)
    return render(request, 'account/profile_update.html', {'form': form})


@login_required
def delete_image(request, username):
    user = MyUser.objects.get(username=username)
    user.image.delete()
    return redirect('account:user_panel', username)


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
    paginate_by = 1
    model = CommentBaseClass
    context_object_name = 'comments'

    def get_queryset(self):
        get_article_comments = ArticleComment.objects.filter(email=self.request.user.email).order_by('-created_at', )
        get_course_comments = CourseComment.objects.filter(email=self.request.user.email).order_by('-created_at', )
        queryset = list(get_article_comments) + list(get_course_comments)

        # queryset = CommentBaseClass.objects.filter(email=self.request.user.email).order_by('-created_at', )
        return queryset


def delete_comment(request, username, id):
    comment = get_object_or_404(CommentBaseClass, id=id)
    comment.delete()
    return redirect('account:user_panel_comments', username)


class TicketView(View):
    def get(self, request, username):
        user = MyUser.objects.get(username=username)
        tickets = user.user_tickets.all()
        return render(request, 'account/profile_ticket.html', {'tickets': tickets})

    def post(self, request, username):
        title, desc = request.POST.get('title'), request.POST.get('desc')
        Ticket.objects.create(user=request.user, title=title, description=desc)
        return redirect('account:user_panel_ticket', username)


def logout_view(request):
    logout(request)
    return redirect('home')
