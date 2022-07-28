from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

# default
class StudentListView(ListView):
    model = Student

#custom
class StudentListView(Listview):
    model = Student
    template_name_suffix = "_get" #by default it is "_list"----now that we have changed it to "_get" we can rename the template file to student_get.html---helps to manage the large project with hundreds of html page
    template_name = "student.html" #can name your template student.html now....prefered way to do it
    context_object_name = "students" #no need to write student_list or object_list in html now
    order = ["roll"] #display in sorted order by roll

    def get_queryset(self):
        return Student.objects.filter(course="cse") #only return student with cse in context
        #different methods---do----