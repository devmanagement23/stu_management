from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,"students/home.html",)

def add_student(request):
    return render(request,"students/add_student.html")