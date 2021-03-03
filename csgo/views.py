from django.shortcuts import render, redirect
from .models import CsgoPlayer
from .forms import SelectPlayers
from .generate_team import generate
from django.contrib import messages

def show_csgo_stats(request):
    
    player_data = CsgoPlayer.objects.order_by("-elo")

    player_list_ranked = []
    player_list_unranked = []

    for player in player_data:
        if player.playes_matches >= 10:
            player_list_ranked.append(player)
        else:
            player_list_unranked.append(player)

    return render(request, "csgo/show_csgo_stats.html", {"player_data_ranked": player_list_ranked, "player_data_unranked": player_list_unranked})

def select_players(request):

    if request.method == "POST":

        form = SelectPlayers(request.POST)
        if form.is_valid():
            selected_players = form.clean()

            player_dict = {}
            queryset = None

            for dict in selected_players:
                queryset = selected_players[dict]

            for item in queryset:
                player_dict[item.name] = item.elo

            if len(player_dict) >= 4:
            
                team_a, team_b = generate(player_dict)
            
                return render(request, "csgo/show_teams.html", {"team_a": team_a, "team_b": team_b})
            
            else:

                messages.warning(request, "Bitte wählen Sie mindestens 4 Spieler aus!")
                
                return redirect("select_players")

    else:

        selectform = SelectPlayers()
        
        return render(request, "csgo/select_players.html", {"selectform": selectform})