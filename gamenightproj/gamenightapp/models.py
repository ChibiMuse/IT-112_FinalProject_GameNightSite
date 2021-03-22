from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GameGenres(models.Model):
    gamegenre=models.CharField(max_length=255)

    def __str__(self):
        return self.gamegenre
    
    class Meta:
        db_table='gamegenre'
        verbose_name_plural='gamegenres'

class Publishers(models.Model):
    publishername=models.CharField(max_length=255)

    def __str__(self):
        return self.publishername
    
    class Meta:
        db_table='publisher'
        verbose_name_plural='publishers'

class GameTypes(models.Model):
    gametype=models.CharField(max_length=255)

    def __str__(self):
        return self.gametype
    
    class Meta:
        db_table='gametype'
        verbose_name_plural='gametypes'

class Games(models.Model):
    gametitle=models.CharField(max_length=255)
    gamegenre=models.ManyToManyField(GameGenres)
    gametype=models.ManyToManyField(GameTypes)
    minplayers=models.IntegerField()
    maxplayers=models.IntegerField()
    playtime=models.DurationField()
    minage=models.IntegerField()
    publishdate=models.DateField()
    publisher=models.ForeignKey(Publishers, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.gametitle
    
    class Meta:
        db_table='game'
        verbose_name_plural="games"


class Inventory(models.Model):
    lastplayeddate=models.DateField()
    game=models.ForeignKey(Games, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.game + self.user + '-' + self.lastplayeddate
    
    class Meta:
        db_table='inventory'
        verbose_name_plural='inventories'

class FriendsList(models.Model):
    user=models.ForeignKey(User, related_name='FriendsList',on_delete=models.CASCADE)
    friend=models.ForeignKey(User, related_name='friends',on_delete=models.CASCADE)
    frienddate=models.DateField()

    def __str__(self):
        return self.user + '-' + self.friend + '_' + self.frienddate
    
    class Meta:
        db_table='FriendList'
        verbose_name_plural='FriendLists'


