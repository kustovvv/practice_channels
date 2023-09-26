from django.shortcuts import render

from .models import Rooms, Message

def rooms(request):
    rooms = Rooms.objects.all()
    return render(request, 'room/rooms.html', {'rooms': rooms})

def details(request, slug):
    room = Rooms.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)
    return render(request, 'room/details.html', {'room': room, 'messages': messages})