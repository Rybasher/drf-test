from rest_framework import serializers 

from ..models.player_skill import PlayerSkill

class PlayerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSkill
        fields = ['id', 'skill', 'value']
