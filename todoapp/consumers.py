from email import message
import json
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync import async_to_sync
import asyncio
class  MySyncConsumer(WebsocketConsumer):

    def connect(self):
        print("Channel Name:",self.channel_name)
        print("Channel Name:",self.channel_layer)
        print("it is Connected")
        print("#######CONNECTED############")
        self.group_name=self.scope['url_route']['kwargs']['gre']
        print(self.group_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
            )
        self.accept()
    def receive(self, text_data=None, bytes_data=None):
        print("Data from Client ...",text_data)
        async_to_sync(self.channel_layer.group_send)(
            'todoapp',
            {
                'type':'chat.message',
                 'mesg':'Your data is stored '
            }
        )
    def chat_message(self,event):
        print("Event...",event)
        self.send(text_data=json.dumps({
            'msg':event['mesg']
        }))        
    
    def disconnect(self, close_code):
        print("WebSocket Disconnected")