from django.db import models

class Tokens(models.Model):
    name = models.CharField(max_length=50)
    damage = models.IntegerField()
    cost = models.IntegerField()
