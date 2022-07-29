from django.shortcuts import render
from .models import Student
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from django import forms

# Create your views here.
class StudentDeleteView(DeleteView):
    model = Student
    success_url = "/deleted/"

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = "/thanks/"

    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
        form.fields['email'].widget = forms.TextInput(attrs = {'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'myclass'})
        return form

class ThanksView(TemplateView):
    template_name = "school/thanks.html"

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = "/success/"
    
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
        form.fields['email'].widget = forms.TextInput(attrs = {'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'myclass'})
        return form


class UpdateView(TemplateView):
    template_name = "school/update_success.html"

class DeleteView(TemplateView):
    template_name = "school/deleted.html"
    