from django.shortcuts import render
from .models import CsgoPlayer

def show_csgo_stats(request):
    
    player_data = CsgoPlayer.objects.order_by("-elo")

    return render(request, "csgo/csgo_stats_show.html", {"player_data": player_data})
