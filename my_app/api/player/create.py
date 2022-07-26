## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, serializers
from my_app.models.player import Player
from my_app.serializers.player import PlayerSerializer
from django.core.exceptions import ValidationError

def create_player_handler(request: Request):
    try:
        player = PlayerSerializer(data=request.data)
        existing_player = Player.objects.filter(
            name=request.data['name'],
            position=request.data['position']
        ).exists()
        if existing_player:
            raise serializers.ValidationError('This player already exists')
        if player.is_valid():
            player.save()
            return Response(player.data)
    except ValidationError as e:
        return Response({'message': e.messages[0]}, status=status.HTTP_400_BAD_REQUEST)
        