from django.shortcuts import render
from .models import Games, GameTypes, GameGenres, Inventory, FriendsList

# Create your views here.
def index(request):
    return render(request, 'gamenightapp/index.html')

def getgames(request):
    games_list=Games.objects.all()
    return render(request, 'gamenightapp/games.html', {'games_list' : games_list})