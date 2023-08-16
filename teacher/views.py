from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, View
from .models import *
from .forms import *


class TeachPageView(View):
    def get(self, request):
        rules = TeachRule.objects.all()
        form = TeachRequestForm
        teachers = Teacher.objects.all()
        return render(request, 'teacher/teach_request.html', {'rules': rules, 'form': form, 'teachers': teachers})

    def post(self, request):
        form = TeachRequestForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            TeachRequest.objects.create(**cd)
        return JsonResponse({'status': 'success'})
