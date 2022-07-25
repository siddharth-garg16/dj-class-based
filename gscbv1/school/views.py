from ssl import HAS_TLSv1_1
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

#function based view
def myview(request):
    return HttpResponse("<h1>Function Based View.</h1>")


#class based view
class MyView(View):
    def get(self, request):
        return HttpResponse("<h1>Class Based View.</h1>")