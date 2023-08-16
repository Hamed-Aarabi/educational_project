from django.urls import path
from . import views

app_name = 'teacher'
urlpatterns = [
    path('', views.TeachPageView.as_view(), name='teach_page'),

]
