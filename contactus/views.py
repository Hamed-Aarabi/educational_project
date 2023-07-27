from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import ContactusForm, Contactus



class ContactusView(FormView):
    template_name = 'contactus/contactus.html'
    form_class = ContactusForm
    success_url = reverse_lazy('contactus:create')

    def form_valid(self, form):
        cd = form.cleaned_data
        Contactus.objects.create(full_name=cd['full_name'], email=cd['email'], subject=cd['subject'], text=cd['text'])
        return super(ContactusView, self).form_valid(form)


