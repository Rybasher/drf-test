from django.db import models
from django.core.exceptions import ValidationError
from .player import Player

class PlayerSkill(models.Model):
    player = models.ForeignKey(Player, related_name='playerSkills', on_delete=models.CASCADE)
    skill = models.CharField(max_length=16, blank=False)
    value = models.IntegerField()

    def clean(self):
        if self.skill not in ('defense', 'attack', 'speed', 'strength', 'stamina'):
            raise ValidationError({
                'message': f'Invalid value for skill: {self.skill}'
            })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.skill
