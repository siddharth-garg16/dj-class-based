from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required


#method 1 of doing this on class based views
@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = "registration/profile.html"