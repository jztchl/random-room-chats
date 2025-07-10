
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.db import transaction
from chat.models import Room    
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"{self.room_name}"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        with transaction.atomic():
            room,created= Room.objects.get_or_create(name=self.room_group_name)
            if created:
                print("Room created")
            room.members = room.members + 1
            room.save()
        
            
        self.accept()
        
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
        with transaction.atomic():
            try:
                room = Room.objects.get(name=self.room_group_name)
                room.members = room.members - 1
                room.save(update_fields=['members'])
                if room.members == 0:
                    room.delete()
                    print("Room deleted")
            except Room.DoesNotExist:
                print("Room does not exist")
            
        
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat.message", "message": message}
        )
    def chat_message(self, event):
        message = event["message"]
        self.send(text_data=json.dumps({"message": message}))
        