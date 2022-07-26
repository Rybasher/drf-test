## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from my_app.models.player import Player
from my_app.serializers.player import PlayerSerializer

def get_player_list_handler(request: Request):
    players = Player.objects.filter(**request.query_params.dict()) if request.query_params \
        else Player.objects.all()
    if players:
        serialized_players = PlayerSerializer(players, many=True)
        return Response(serialized_players.data)
    return Response(status=status.HTTP_404_NOT_FOUND)
