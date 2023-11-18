from typing import Text
from django import forms
from django.forms import fields
from django.forms.widgets import Widget

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
#from importlib_metadata import email
from .models import Student,Teacher,All_Course,User_Course,Message

from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    email= forms.EmailField(required=True)
    class Meta:
        model= User
        fields= ["username","email", "password1", "password2",]


class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields= [f"{CreateUserForm.Meta.fields.__getitem__(0)}",f"{CreateUserForm.Meta.fields.__getitem__(1)}",]

class TeacherForm(CreateUserForm):
    class Meta:
        model= Teacher
        fields =  [f"{CreateUserForm.Meta.fields.__getitem__(0)}",f"{CreateUserForm.Meta.fields.__getitem__(1)}",]




class CourseForm(forms.ModelForm):
    class Meta:
        model= All_Course
        fields =  ["identification_code","title","description","price",]

class Pdf_Form(forms.ModelForm):
    class Meta:
        model=All_Course
        fields= ["pdf_file"]
class Video_Form(forms.ModelForm):
    class Meta:
        model=All_Course
        fields= ["video_file"]


class User_Course_Form(forms.ModelForm):
    class Meta:
        model= User_Course
        fields =  [f"{CreateUserForm.Meta.fields.__getitem__(0)}","course_id_title",]





from django import forms

from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model=Payment
        fields=["amount","email"]
