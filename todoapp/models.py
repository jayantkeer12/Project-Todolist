from email.policy import default
from importlib.resources import contents
from tkinter import Widget
from django import forms
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
class NewUser(models.Model):
    e_mail=models.EmailField(primary_key=True,max_length=40)
    pass_word=models.CharField(max_length=20)
class TodoListIteam(models.Model):
    e_mail=models.EmailField(max_length=45)
    content =models.CharField(max_length=50)
    name=models.CharField(max_length=40,default="")
    image = models.URLField(default="") 

class UploadImage(models.Model):
    image = models.ImageField(upload_to='myimage/',default="")