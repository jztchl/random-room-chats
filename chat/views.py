from django.http import JsonResponse
from chat.models import Room

def list_active_rooms(request):
    rooms = Room.objects.all()
    return JsonResponse({'active_rooms': [room.name for room in rooms]})