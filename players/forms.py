from django import forms
from .models import Player

# PLAYER_CHOICES = (
#     Player.objects.all().values_list('id', 'name')
# )

class PlayerSearchForm(forms.Form):
    # search = forms.CharField(max_length=100)
    player = forms.ModelChoiceField(queryset=Player.objects.all())
    # player = forms.ChoiceField(choices=PLAYER_CHOICES)

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['name', 'nickname', 'phone', 'email', 'birth_date', 'favorite_team', 'photo', 'position']
