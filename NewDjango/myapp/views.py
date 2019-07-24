from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def index(request):
    return render(request,"test.html")


def test(request):
    request.session['user'] ='saveen'
    request.session['hello_user'] = "Default User"
    del request.session['user']
    test = request.session.get('user', 'hello')

    # student_object= student(
    #     name="Hari",
    #     address="Patan"
    # )
    # student_object.save()
    # value = student.objects.get(name="Hari")
    # address=value.address
    return render(request,"test.html",{"user":test})

def home(request):
    if request.method =="POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/contactus')
    else:
        form = StudentForm()
        return render(request,"Home.html",{'form':form})


def contactus(request):
    students = Student.objects.all()
    return render(request,"Contact Us.html",{'students': students})


def delete(request,id):
    student =  Student.objects.get(id=id)
    student.delete()
    return redirect("/contactus")

def update(request, id):
    student = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance = student)
    if form.is_valid():
        form.save()
        return redirect("/contactus")
    return render(request,"edit.html",{'student':student})


def edit(request,id):
    student = Student.objects.get(id=id)
    return render(request,"edit.html",{'student':student})
