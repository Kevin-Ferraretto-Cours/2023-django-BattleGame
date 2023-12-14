from django.db import models
from characters.models import Character
from django.contrib.auth.models import User

class Game(models.Model):
    
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    typePersonnage = models.CharField(max_length=25, choices=Character.TypeChoiceCharacter.choices, default= Character.TypeChoiceCharacter.Archer)
    idPersonnage = models.IntegerField()
    state = models.IntegerField(default=0)
    idEnemy = models.IntegerField(blank=True, null=True)
    enemyHp = models.IntegerField(blank=True, null=True)
    enemyMaxHp = models.IntegerField(blank=True, null=True)
    enemyDamage = models.IntegerField(blank=True, null=True)
    historique = models.JSONField(default=dict)
