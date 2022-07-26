from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView

#if we don't want to write redirect view in urls.py
class GoogleRedirectView(RedirectView):
    url = "https://www.google.com"


