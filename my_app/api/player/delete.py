from django.shortcuts import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from my_app.models import Player
from rest_framework import status
from typing import Any  

def delete_player_handler(request: Request, id: Any) -> Response:
    item = get_object_or_404(Player, pk=id)
    item.delete()
    return Response({"message": f"User with {id} id is deleted"}, status=status.HTTP_202_ACCEPTED)
