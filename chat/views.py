from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render

from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import ChatGrant

from .models import Room

fake = Faker()


def all_rooms(request):
    rooms = Room.objects.all()
    return render(request, 'chat.html', {'rooms': rooms})


def room_detail(request, slug):
    room = Room.objects.get(slug=slug)
    return render(request, 'room_detail.html', {'room': room})


def token(request):
    identity = request.GET.get('identity', fake.user_name())
    device_id = request.GET.get('device', 'default')  # unique device ID

    account_sid = 'AC82a278d0019838fec847a68c5d0c0726'
    api_key = 'SKb1ef123dc72810def5be32dc47eb51f8'
    api_secret = 'e11c019c793c4068c2c401f94d52'
    chat_service_sid = 'IS59bf80081bc4466c8fec97ecbe35f4ea'

    token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    endpoint = "MyDjangoChatRoom:{0}:{1}".format(identity, device_id)
    # Create a Chat grant and add to token
    if chat_service_sid:
        chat_grant = ChatGrant(endpoint_id=endpoint,
                               service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    # Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt().encode().decode('utf-8')})
