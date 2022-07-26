from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from my_app.models.player_skill import PlayerSkill
from my_app.models.player import Player
from collections import Counter
from my_app.serializers.player import PlayerSerializer
from django.core.exceptions import ValidationError


def positions_validation(request_data: list) -> None:
    positions = [item['position'] for item in request_data]
    positions_counter = Counter(positions)
    if positions_counter.most_common()[0][1] > 1:
        raise ValidationError({
            "message": "You specified two identical positions"
        })
    

def team_process_handler(request: Request) -> Response:
    try:
        positions_validation(request_data=request.data)
    except ValidationError as e:
        return ValidationError({
                "message": e.messages[0]
            }, status=status.HTTP_400_BAD_REQUEST
        )
    
    if not Player.objects.all():
        return Response({
                "message": 'No players'
            }, status=status.HTTP_404_NOT_FOUND
        )
    
    players_list: list = []
    
    for item in request.data:
        players = Player.objects.filter(position=item['position'], playerSkills__in=PlayerSkill.objects.filter(
            skill=item['mainSkill']
        )).order_by('-playerSkills__value')
        players_desired = item['numberOfPlayers']
        if players:
            players_serialized = PlayerSerializer(players, many=True) if players.count() < players_desired \
                else PlayerSerializer(players[0: players_desired], many=True) 
            players_list.append(players_serialized.data)
        else:
            players = Player.objects.filter(position=item['position']).order_by('-playerSkills__value')
            if players.count() < 1:
                players = Player.objects.all().order_by('-playerSkills__value')
            players_serialized = PlayerSerializer(players[0])
            players_list.append([players_serialized.data])

    return Response(sum(players_list, []), status=200)
