from django.contrib import admin
from my_app.models import player, player_skill

# Register your models here.


admin.site.register(player_skill.PlayerSkill)
admin.site.register(player.Player)