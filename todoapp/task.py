from pickle import TRUE
from telnetlib import STATUS
from PIL import Image
from pytesseract import pytesseract
from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from todoapp.consumers import MySyncConsumer
from todoproject.settings import CHANNEL_LAYERS
# Create your tests here.
from .models import TodoListIteam
from celery import Celery,shared_task
import todoapp.views
from channels.layers import get_channel_layer
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
status=True  
@shared_task(bind=True)
def test_fun(self,url,id1):
    #print(url,"____+======")
    #if url.find(".png")!=-1 or url.find(".jpeg")!=-1 or url.find(".gif")!=-1 or url.find(".JPG")!=-1 or url.find(".jpg")!=-1 or url.find(".jfif")!=-1:
    #        pass
    #else:
    #    name=TodoListIteam.objects.get(image=url) 
     #   name.image="not allowed"
     #   name.save()
     #   print("This file is not image format") 
      #  return False
    #return url
     if not url== None:
            path_to_image ="D:/Experiment/todoproject"+url
            print(path_to_image)
            try:
                Image.open(path_to_image)
            except:
                name=TodoListIteam.objects.get(image=url) 
                name.image="not allowed"
                name.save()
                print('sorry, your image is invalid')
                return [False]
            return [url,id1]
@shared_task(bind=True)
def test_fun2(self,url):
    if url[0] is not False:
        global status
        path_to_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        path_to_image ="D:/Experiment/todoproject"+url[0]
        pytesseract.tesseract_cmd=path_to_tesseract
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        print('------------H')
        async_to_sync(CHANNEL_LAYERS.group_send)({"type": "chat.force_disconnect"})
        print(text,"-----------",status)
        return  status
    else:
        return False
