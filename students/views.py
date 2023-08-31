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


def delete_student(request,roll):
    s = Student.objects.get(pk=roll)
    s.delete()

    return redirect("/students/home")

def update_student(request,roll):
    ss = Student.objects.get(pk=roll)
    return render(request,'students/updating_student.html',{'studentDetail':ss})

def do_update_student(request,roll):
    #retreive the user inputs
        student_roll_update = request.POST.get("std_roll")
        student_name_update = request.POST.get("std_name")
        student_email_update = request.POST.get("std_email")

        #donot create new object , get already filled element from database
        sm=Student.objects.get(pk=roll)

        sm.roll = student_roll_update
        sm.name = student_name_update
        sm.email = student_email_update

        sm.save()

        return redirect("/students/home")
