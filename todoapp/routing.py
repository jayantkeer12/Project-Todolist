from django.urls import path
from .import consumers,task
websocket_urlpatterns=[
    #path('ws/sc/<str:gre>/',consumers.MySyncConsumer.as_asgi()),
    path('ws/sc/todoapp/',consumers.MySyncConsumer.as_asgi()),
    path('ws/awsc/todoapp/',consumers.AsyncWebsocketConsumer.as_asgi()),
]