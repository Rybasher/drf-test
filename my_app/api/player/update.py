## /////////////////////////////////////////////////////////////////////////////
## YOU CAN FREELY MODIFY THE CODE BELOW IN ORDER TO COMPLETE THE TASK
## /////////////////////////////////////////////////////////////////////////////

from django.http.response import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from my_app.models.player import Player
from my_app.serializers.player import Player, PlayerSerializer
from typing import Any
from django.shortcuts import get_object_or_404

def update_player_handler(request: Request, id: Any) -> Response:
    current_player = get_object_or_404(Player, pk=id)
    player = PlayerSerializer(instance=current_player, data=request.data)
    if player.is_valid():
        player.save()
    return Response(player.data)
        

