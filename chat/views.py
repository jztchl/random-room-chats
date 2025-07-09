from django.http import JsonResponse
from chat.models import Room

def list_active_rooms(request):
    rooms = Room.objects.all()
    if not rooms:
        return JsonResponse([], safe=False)
    data = [{'name': room.name, 'active_members': room.members} for room in rooms]
    return JsonResponse(data, safe=False)