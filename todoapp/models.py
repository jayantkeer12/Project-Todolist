from importlib.resources import contents
from django.db import models
class TodoListIteam(models.Model):
    content =models.TextField()
