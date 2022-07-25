import django
from django.shortcuts import render
from django.views import View

# Create your views here.
def homefun(request):
    name = "By Function View"
    return render(request, 'school/home.html', {'name':name})

class HomeClassView(View):
    def get(self, request):
        name = "By Class Based View"
        return render(request, 'school/home.html', {'name':name})
        
