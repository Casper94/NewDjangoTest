from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
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
        name = request
    else:

    form = StudentForm()
    return render(request,"Home.html",{'form':form})


def contactus(request):
    form= StudentForm()
    return render(request,"Contact Us.html",{'form':form})
