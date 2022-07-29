from django.db import models
from django.urls import reverse
from django import forms

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    password = models.CharField(max_length=70)
    
    #to add css to these fields we need classes--helps us to do that--same as before
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs = {'class':'myclass'})
        form.fields['email'].widget = forms.TextInput(attrs = {'class':'myclass'})
        form.fields['password'].widget = forms.PasswordInput(attrs = {'class':'myclass'})
        #can give placeholders as well etc etc


        #we can do above things in simpler way if we create a form in forms.py and just import it in views and use it instead of model = student there
    def get_absolute_url(self):
        return reverse("thanks")