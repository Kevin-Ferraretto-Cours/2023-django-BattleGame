from django.db import models

class Weapon(models.Model):
    
    class TypeChoiceWeapon(models.TextChoices):
        Bow = "Bow"
        Staff = "Staff"
        Mass = "Mass"
        Shield = "Shield"
        Hatchet = "Hatchet"
        
    class StarterChoiceWeapon(models.IntegerChoices):
        Vrai = 1
        Faux = 0
    
    starter = models.IntegerField(choices=StarterChoiceWeapon.choices, default=StarterChoiceWeapon.Faux)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=25, choices=TypeChoiceWeapon.choices)
    damage = models.IntegerField()
    defense = models.IntegerField()
    
    def __str__(self):
        return self.name
