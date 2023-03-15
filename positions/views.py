from django.shortcuts import render
from .models import Position

# Create your views here.

def home_view(request):
    positions = Position.objects.all()
    return render(request, 'positions/main.html', {'positions': positions})
