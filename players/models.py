from django.db import models
from positions.models import Position
from django.shortcuts import reverse

# Create your models here.

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birth_date = models.DateField()
    favorite_team = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='players')
    # create position field as a foreign key
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("players:player-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} - {self.nickname}"