from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def homefun(request):
    name = "By Function View"
    return render(request, 'school/home.html', {'name':name})

class HomeClassView(View):
    def get(self, request):
        name = "By Class Based View"
        return render(request, 'school/home.html', {'name':name})

#########################################################

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
        return HttpResponse('<h1>Thanks!</h1>')
    else:
        form = ContactForm()
    return render(request, 'school/contact.html', {'form':form})


class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'school/contact.html', {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
        return HttpResponse('<h1>Thanks!</h1>')


        
