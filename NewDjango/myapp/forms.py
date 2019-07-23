from django.forms import forms
from .models import Student


class StudentForm(forms):
    class meta:
        model = Student
        fields = "__all__"