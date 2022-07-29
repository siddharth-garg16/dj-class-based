from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms


# Create your views here.
class StudentFormCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    #can use template_name here too
    # success_url = "/thanks/"

    #to add css to these fields we need classes--helps us to do that--same as before
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
        form.fields['email'].widget = forms.TextInput(attrs = {'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'myclass'})
        return form
        #can give placeholders as well etc etc
        #we can do above things in simpler way if we create a form in forms.py and just import it in views and use it instead of model = student there

class ThanksTemplateView(TemplateView):
    template_name = "school/thanks.html"
