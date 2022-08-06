from asyncio import tasks
from itertools import chain
from pyexpat import model
import smtplib
import random
from urllib import request
from django import http
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from PIL import Image
from todoapp import task
from todoapp.models import NewUser, TodoListIteam
from todoapp.task import test_fun, test_fun2
from django.core.files.storage import FileSystemStorage
from celery import Task, chain
email=""
otp=0
id1=10
def home(request):
    return render(request,'home.html')
def LogOut(request):
    return render(request,'home.html')
def Forgot(request):
    return render(request,'Forgot.html')

#   for getiing the exact data of task constrain is email id and send that data to html page
def todoappview(request):
    global email
    all_todo_iteams=TodoListIteam.objects.filter(e_mail=email)
    return render(request,'todolist.html',
    {'all_items':all_todo_iteams})
def addTodoItem(request):
    x=request.POST['content']
    if request.method=="POST" and request.FILES.get('img'):
        global id1,status
        img=request.FILES['img']
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        url=fs.url(filename)
        new_item=TodoListIteam(content=x,e_mail=email,image=url)
        new_item.save()
        text=chain(test_fun.s(url,id1),test_fun2.s()).apply_async()
        print( text.info == str('True'),"--------------")
        return HttpResponseRedirect('/todoapp/')
    else:
        return HttpResponseRedirect('/todoapp/')
def deleteTodoItem(request,i):
    global id1
    id1=i
    y=TodoListIteam.objects.get(id=i)
    y.delete()
    print(task.status,"_______:::")
    return HttpResponseRedirect('/todoapp/')
def Register(request):
    return render(request,'Register.html')
def NewRegister(request):
    global email
    if request.method=='POST':
        e_mail2=request.POST.get('email')
        email=e_mail2  
        pass_word2=request.POST.get('psw')
        if NewUser.objects.filter(e_mail=e_mail2):
            return render(request,'UserExist.html')
        else:
            new_obj=NewUser(e_mail2,pass_word2)
            new_obj.save()
            return render(request,'todolist.html')       
    else:
        return render(request,'Register.html')

#verifcation of user by email and password entered right or not
def Verify(request):
    if request.method=='POST':
        global email
        email=request.POST.get("email")
        passWord=request.POST.get('psw')
        try:
            if NewUser.objects.get(e_mail=email) and NewUser.objects.filter(pass_word=passWord):    
                return HttpResponseRedirect('/todoapp/')
            else:
                return render(request,'WrongInput.html')    
        except NewUser.DoesNotExist:
            return HttpResponse("User not Exist")
    return render(request,'home.html')
# sending OTP to user by email
def send_gmail(request):
    global otp
    global email
    otp=random.randint(100,1000)
    print(otp,"    send")
    email=request.POST.get("email")
    print(email,"     email     ")
    if request.method=='POST':
        mail=request.POST.get("email")
        subject="PassWord"
        message="here is your  Otp= "+str(otp)
    try:
       if NewUser.objects.get(e_mail=mail):
            send_mail(subject,message,'jayantkeer4@gmail.com',[mail],fail_silently=False)
            print(otp,"      F       ")        
            return render(request,'EnterOtp.html')
    # if email is wrong we will print this message
    except NewUser.DoesNotExist:
            return HttpResponse("User not Exist")
    else:
        return render(request,'Forgot.html')
def Otp_Confirm(request):
    global otp
    match=request.POST.get("OTP")
    if otp==int(request.POST.get("OTP")):
        return render(request,'change_psw.html')
    else:
        return render(request,'OTPMsg.html')
def Chang_psw(request):
    global email
    if request.method=='POST': 
        psw=request.POST.get("psw")
        temp=NewUser.objects.get(e_mail=email)
        temp.pass_word=psw
        temp.save()
        return HttpResponse('Your password has changed ')