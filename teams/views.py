from django.shortcuts import render
from .models import Team

# Create your views here.

def home_view(request):
    teams = Team.objects.all()
    return render(request, 'teams/main.html', {'teams': teams})
