from django.db import models
from django.core.exceptions import ValidationError

class Player(models.Model):
    name = models.CharField(max_length=64, blank=False, default='')
    position = models.CharField(max_length=16, blank=False)

    def clean(self):
        if self.position not in ('defender', 'midfielder', 'forward'):
            raise ValidationError({
                'message': f'Invalid value for position: {self.position}'
            })
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name