from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes
from my_app.permissions import PermissionAccess
from .api.player.create import create_player_handler
from .api.player.delete import delete_player_handler
from .api.player.get_list import get_player_list_handler
from .api.player.update import update_player_handler
from .api.team.process import team_process_handler


@api_view(['GET', 'POST'])
def player_collection(request: Request):
    if request.method == 'GET':
        return get_player_list_handler(request)
    elif request.method == 'POST':
        return create_player_handler(request)


@api_view(['PUT', 'DELETE'])
@permission_classes([PermissionAccess])
def player(request: Request, id):
    if request.method == 'PUT':
        return update_player_handler(request, id)
    elif request.method == 'DELETE':
        return delete_player_handler(request, id)


@api_view(['POST'])
def team_process(request: Request):
    if request.method == 'POST':
        return team_process_handler(request)

