from django.db import models
from teams.models import Team
from players.models import Player


# Create your models here.

class Match(models.Model):
    id = models.AutoField(primary_key=True)
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    date = models.DateField()
    home_team_players = models.ManyToManyField(Player, related_name='home_team_players')
    away_team_players = models.ManyToManyField(Player, related_name='away_team_players')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.home_team} x {self.away_team}"