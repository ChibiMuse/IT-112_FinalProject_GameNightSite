from django.contrib import admin
from .models import Games, GameGenres, GameTypes, Inventory, FriendsList, Publishers

# Register your models here.
admin.site.register(Games)
admin.site.register(GameGenres)
admin.site.register(GameTypes)
admin.site.register(Inventory)
admin.site.register(FriendsList)
admin.site.register(Publishers)
