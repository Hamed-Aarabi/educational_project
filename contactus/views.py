from django.shortcuts import render
from django.views.generic import FormView, View
from .forms import *
from django.http import JsonResponse


class ContactusView(View):
    def get(self, request):
        form = ContactusForm
        return render(request, 'contactus/contactus.html', {'form': form})

    def post(self, request):
        form = ContactusForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Contactus.objects.create(full_name=cd['full_name'], email=cd['email'], subject=cd['subject'],
                                     text=cd['text'])
        return JsonResponse({'status': 'success'})
