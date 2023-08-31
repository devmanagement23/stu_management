from django.shortcuts import render,redirect
from .models import Student

# Create your views here.


# def home (request):
#     return render(request,"students/home.html",)

def home (request):

    totalstudent = Student.objects.all()

    return render(request,"students/home.html",{'studentall':totalstudent})


def add_student(request):
    if request.method=='POST':
        print("Added")
        #retreive the user inputs
        student_roll = request.POST.get("std_roll")
        student_name = request.POST.get("std_name")
        student_email = request.POST.get("std_email")

        #create an object for models
        s=Student()
        s.roll = student_roll
        s.name = student_name
        s.email = student_email

        s.save()

        return redirect("/students/home")

    # this bleow return line is like  ELSE part.
    return render(request,"students/add_student.html")
