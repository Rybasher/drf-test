from rest_framework import serializers 

from .player_skill import PlayerSkillSerializer
from ..models.player import Player
from ..models.player_skill import PlayerSkill

class PlayerSerializer(serializers.ModelSerializer):

    playerSkills = PlayerSkillSerializer(
        many=True, read_only=False
    )

    def create(self, validated_data):
        skills_data = validated_data.pop('playerSkills')
        player = Player.objects.create(**validated_data)
        for skill in skills_data:
            PlayerSkill.objects.create(player_id=player.id, **dict(skill))

        return player

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.position = validated_data.get('position', instance.position)
        skills_data = validated_data.pop('playerSkills')
        PlayerSkill.objects.all().delete()
        for skill in skills_data:
            PlayerSkill.objects.create(player_id=instance.id, **dict(skill))
        return instance

    class Meta:
        model = Player
        fields = ['id', 'name', 'position', 'playerSkills']
