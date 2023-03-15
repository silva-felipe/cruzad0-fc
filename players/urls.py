from django.urls import path
from .views import (
    # home_view,
    PlayerListView,
    PlayerDetailView,
    search_view,
    player_detail,
    update_player,
)
app_name = 'players'

urlpatterns = [
    # path('', home_view, name='home'),
    path('', search_view, name='players-home'),
    path('search/', search_view, name='player-search'),
    path('<int:pk>/', update_player, name='player-detail'),

]
