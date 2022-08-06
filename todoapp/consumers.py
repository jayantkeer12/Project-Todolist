from channels.consumer import SyncConsumer,AsyncConsumer
from channels.generic.websocket import WebsocketConsumer,AsyncWebsocketConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync import async_to_sync
import asyncio
class  MySyncConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        print("Channel Name:",self.channel_name)
        print("it is Connected")
        print("#######CONNECTED############")

    def disconnect(self, close_code):
        print("WebSocket Disconnected")
        

    def receive(self, text_data=None, bytes_data=None):
        print("Data from Client ...",text_data)
        self.send(text_data="message from server"+text_data)
        async_to_sync(self.channel_layer.group_send)(
            "chat",
            {
                "type": "chat.message",
                "text": text_data,
            },)
