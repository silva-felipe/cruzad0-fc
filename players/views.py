from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Player
from django.views.generic import ListView, DetailView
from .forms import PlayerSearchForm, PlayerForm

# Create your views here.

# def home_view(request):
#     players = Player.objects.all()
#     return render(request, 'players/main.html', {'players': players})

def search_view(request):
    form = PlayerSearchForm(request.GET or None)
    players = Player.objects.all()
    context = {
        'form': form,
        'players': players,
    }
    return render(request, 'players/search.html', context)

class PlayerListView(ListView):
    model = Player
    template_name = 'players/main.html'
    context_object_name = 'players'
    ordering = ['name']
    paginate_by = 10

class PlayerDetailView(DetailView):
    model = Player
    template_name = 'players/player_detail.html'
    context_object_name = 'player'

def player_detail(request, pk):
    player = get_object_or_404(Player, pk=pk)
    form = PlayerForm(instance=player)
    context = {
        'player': player,
        'form': form,
    }
    return render(request, 'players/player_detail.html', context)

def update_player(request, pk):
    player = Player.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('players:players-home')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/player_detail.html', {'player': player, 'form': form})