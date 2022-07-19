from urllib import request
#from certifi import contents
from django.http import HttpResponseRedirect
from django.shortcuts import render

from todoapp.models import TodoListIteam
def todoappview(request):
    all_todo_iteams=TodoListIteam.objects.all()
    return render(request,'todolist.html',
    {'all_items':all_todo_iteams})
def addTodoItem(request):
    x=request.POST['content']
    new_item=TodoListIteam(content=x)
    print(new_item)
    new_item.save()
    return HttpResponseRedirect('/todoapp/')
def deleteTodoItem(request,i):
    y=TodoListIteam.objects.get(id=i)
    y.delete()
    return HttpResponseRedirect('/todoapp/')