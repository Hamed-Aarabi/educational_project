from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('userpanel/<str:username>/home', views.UserPanelView.as_view(), name='user_panel'),
    path('userpanel/<str:username>/update', views.user_update_view, name='user_panel_update'),
    path('userpanel/<str:username>/delete-image', views.delete_image, name='delete_image'),
    path('userpanel/<str:username>/courses', views.UserCoursesView.as_view(), name='user_panel_courses'),
    path('userpanel/<str:username>/comments', views.UserCommentsView.as_view(), name='user_panel_comments'),
    path('userpanel/<str:username>/comments/delete/<int:id>', views.delete_comment, name='user_panel_del_comments'),
    path('userpanel/<str:username>/tickets/', views.TicketView.as_view(), name='user_panel_ticket'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.MyPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
