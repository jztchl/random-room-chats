from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100,unique=True)
    members = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'chat'
        