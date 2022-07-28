from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView

class StudentDetailView(DetailView):
    model = Student
    # template_name = 'school/student.html' --alows to name our html file--no need to go with the default student_detail---kindof same like list view
    pk_url_kwarg = 'id' #now we can get detail using id in dynamic url
