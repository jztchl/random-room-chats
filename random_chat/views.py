from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import JsonResponse

async def list_active_rooms(request):
    channel_layer = get_channel_layer()
    rooms = await ChatConsumer.list_rooms(channel_layer)
    return JsonResponse({'active_rooms': rooms})