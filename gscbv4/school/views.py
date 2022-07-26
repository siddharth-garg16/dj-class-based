from django.shortcuts import render
from django.views.generic.base import TemplateView

#incase i don't want to write template name in the urls.py file and want to do some additional stuff.
# class HomeTemplateView(TemplateView):
#     template_name = "school/home.html" #this will simply render html page

class HomeTemplateView(TemplateView):
    template_name = "school/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name']='Siddharth'
        context['roll']='30'
        return context

