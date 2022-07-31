from PIL import Image
from pytesseract import pytesseract
from django.contrib.auth import get_user_model
# Create your tests here.
from .models import TodoListIteam
from celery import shared_task
@shared_task(bind=True)
def test_fun(self,url):
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
                return False
            return url
@shared_task(bind=True)
def test_fun2(self,url):
    if url!=False:
        path_to_tesseract=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        path_to_image ="D:/Experiment/todoproject"+url
        pytesseract.tesseract_cmd=path_to_tesseract
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        print(text,"-----------")
        return "-----------Done------------"
    else:
        return "This file is not image"
