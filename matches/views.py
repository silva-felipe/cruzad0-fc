from django.shortcuts import render
from .models import Match

# Create your views here.

def home_view(request):
    matches = Match.objects.all()
    return render(request, 'matches/main.html', {'matches': matches})
