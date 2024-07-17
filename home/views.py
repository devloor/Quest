from django.shortcuts import render, redirect
from home.models import student as Student
from django.contrib import messages

# Create your views here.
def hello_view(request):
    return render(request, 'home/index.html')

def hello(request, name):
    context={"name":name}
    return(request, "home/index.html", context)

def student(request):
    all_students = Student.objects.all()
    context ={'data':all_students}
    return render(request, "home/student.html", context)
def newstud(request):
    if request.method == "POST":
        name= request.POST.get("Name")
        regno= request.POST.get("RegNo")
        dept = request.POST.get("Dept")
        age= request.POST.get("Age")
        cgpa= request.POST.get("CGPA")
        print(name,regno,age,cgpa)
        if not name or not regno or not dept or not age or not cgpa :
            messages.error(request, "All fields are required")
            return redirect(newstud)
        new_student=Student.objects.create(name=name, reg_number =regno, dpt = dept, age =age, cgpa =cgpa)
        new_student.save()
        messages.success(request, "Created successfully")
        return redirect("home")
    return render(request, 'home/newstudent.html')