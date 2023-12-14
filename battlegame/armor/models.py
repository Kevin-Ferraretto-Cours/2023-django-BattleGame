from django.db import models

class Armor(models.Model):
    
    class TypeChoiceArmor(models.TextChoices):
        Helmet = "Helmet"
        Chestplate = "Chestplate"
        Leggings = "Leggings"
        Boots = "Boots"
    
    class StarterChoiceArmor(models.IntegerChoices):
        Vrai = 1
        Faux = 0
    
    name = models.CharField(max_length=100)
    hp = models.IntegerField()
    mana = models.IntegerField()
    rage = models.IntegerField()
    defense = models.IntegerField()
    crit_rate = models.IntegerField()
    crit_dmg = models.IntegerField()
    starter = models.IntegerField(choices=StarterChoiceArmor.choices, default=StarterChoiceArmor.Faux)
    
    class Meta:
        managed = False
    
    def __str__(self):
        return self.name

class Helmet(Armor):
    type = models.CharField(max_length=25, choices=Armor.TypeChoiceArmor.choices, default=Armor.TypeChoiceArmor.Helmet)

class Chestplate(Armor):
    type = models.CharField(max_length=25, choices=Armor.TypeChoiceArmor.choices, default=Armor.TypeChoiceArmor.Chestplate)

class Leggings(Armor):
    type = models.CharField(max_length=25, choices=Armor.TypeChoiceArmor.choices, default=Armor.TypeChoiceArmor.Leggings)

class Boots(Armor):
    type = models.CharField(max_length=25, choices=Armor.TypeChoiceArmor.choices, default=Armor.TypeChoiceArmor.Boots)