from django.db import models

# Create your models here.

class Position(models.Model):
    id = models.AutoField(primary_key=True)
    position_name = models.CharField(max_length=100)
    game_field = models.CharField(max_length=100)

    def __str__(self):
        return self.position_name