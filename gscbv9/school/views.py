from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Student

# Create your views here.
class StudentFormCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    #can use template_name here too
    # success_url = "/thanks/"

class ThanksTemplateView(TemplateView):
    template_name = "school/thanks.html"
