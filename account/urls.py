from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name= 'account'


urlpatterns = [
    path('signup',views.SignUpView.as_view(), name='signup'),
    path('login',views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]