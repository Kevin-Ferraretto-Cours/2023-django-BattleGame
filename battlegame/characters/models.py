from django.shortcuts import get_object_or_404
from math import ceil
import random
from django.db import models
from armor.models import Helmet, Chestplate, Leggings, Boots
from weapon.models import Weapon
from tokens.models import Tokens


class Character(models.Model):
    
    class TypeChoiceCharacter(models.TextChoices):
        Archer = "Archer"
        Magician = "Magician"
        Barbarian = "Barbarian"
        Paladin = "Paladin"
        Monster = "Monster"
    
    
    
    name = models.CharField(max_length=50, default="")
    hp = models.IntegerField()
    defense = models.IntegerField()
    helmet = models.ForeignKey(Helmet, on_delete=models.CASCADE, null=True, blank=True)
    chestplate = models.ForeignKey(Chestplate, on_delete=models.CASCADE, null=True, blank=True)
    leggings = models.ForeignKey(Leggings, on_delete=models.CASCADE, null=True, blank=True)
    boots = models.ForeignKey(Boots, on_delete=models.CASCADE, null=True, blank=True)
    tokensAvailable = models.IntegerField(null=True, blank=True)
    tokens = models.ManyToManyField(Tokens)
    weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE, null=True, blank=True)
    state = models.IntegerField(null=True, blank=True)
    typeCharacter = models.CharField(max_length=25, choices=TypeChoiceCharacter.choices, default= TypeChoiceCharacter.Archer)
    
    class Meta:
        managed = True
        
    def getMaxHp(self):
        return (self.basic_hp + self.helmet.hp + self.chestplate.hp + self.leggings.hp + self.boots.hp)

    def getMaxRage(self):
        return (self.basic_rage + self.helmet.rage + self.chestplate.rage + self.leggings.rage + self.boots.rage)

    def getMaxMana(self):
        return (self.basic_mana + self.helmet.mana + self.chestplate.mana + self.leggings.mana + self.boots.mana)

    def get_defense(self) -> float:
        defense = 0
        if hasattr(self, "shield") and self.shield != None:
            defense += self.shield.defense
        if hasattr(self, "boots") and self.boots != None:
            defense += self.boots.defense
        if hasattr(self, "leggings") and self.leggings != None:
            defense += self.leggings.defense
        if hasattr(self, "chestplate") and self.chestplate != None:
            defense += self.chestplate.defense
        if hasattr(self, "helmet") and self.helmet != None:
            defense += self.helmet.defense
        defense += self.defense
        return defense
    
    def get_crit_rate(self) -> float:
        critRate = 0
        if hasattr(self, "boots") and self.boots != None:
            critRate += self.boots.crit_rate
        if hasattr(self, "leggings") and self.leggings != None:
            critRate += self.leggings.crit_rate
        if hasattr(self, "chestplate") and self.chestplate != None:
            critRate += self.chestplate.crit_rate
        if hasattr(self, "helmet") and self.helmet != None:
            critRate += self.helmet.crit_rate
        return critRate
    
    def get_crit_dmg(self) -> float:
        critDmg = 0
        if hasattr(self, "boots") and self.boots != None:
            critDmg += self.boots.crit_dmg
        if hasattr(self, "leggings") and self.leggings != None:
            critDmg += self.leggings.crit_dmg
        if hasattr(self, "chestplate") and self.chestplate != None:
            critDmg += self.chestplate.crit_dmg
        if hasattr(self, "helmet") and self.helmet != None:
            critDmg += self.helmet.crit_dmg
        return critDmg
    
    def full_heal(self) -> None:
        self.hp = self.getMaxHp()
        self.save()
    
    def full_mana_rage(self) -> None:
        if hasattr(self, "mana"):
            self.mana = self.getMaxMana()
        if hasattr(self, "rage"):
            self.rage = self.getMaxRage()
        self.save()
    
    def damage_reduction(self, damage, enemy) -> float:
        defense = enemy.get_defense()
        return ceil((1-(defense/500)) * damage)
    
    def has_crit(self, damage) -> float:
        if random.random() <= (self.get_crit_rate()/100):
            return ceil(damage * (1+(self.get_crit_dmg()/100)))
        return damage
    
    def takeDamage(self, damage) -> None:
        self.hp -= damage
        self.save()
    
    def getAttack(self) ->int:
        return (self.weapon.damage)
    
class Archer(Character):
    mana = models.IntegerField(default=100)
    basic_mana = models.IntegerField(default=100)
    basic_hp = models.IntegerField(default=200)
    tokens_limit = (3,0) # MAGICAL / PHYSICAL 
    classe_name = "Archer"

class Magician(Character):
    mana = models.IntegerField(default=100)
    basic_mana = models.IntegerField(default=100)
    basic_hp = models.IntegerField(default=200)
    tokens_limit = (3,0) # MAGICAL / PHYSICAL 
    classe_name = "Mage"

class Barbarian(Character):
    rage = models.IntegerField(default=100)
    basic_rage = models.IntegerField(default=100)
    basic_hp = models.IntegerField(default=300)
    tokens_limit = (0,3) # MAGICAL / PHYSICAL
    classe_name = "Barbarian"
    
    def getAttack(self) ->int:
        return (self.weapon.damage * 2)

class Paladin(Character):
    rage = models.IntegerField(default=50)
    basic_rage = models.IntegerField(default=50)
    basic_hp = models.IntegerField(default=300)
    tokens_limit = (0,3) # MAGICAL / PHYSICAL 
    classe_name = "Paladin"
    shield = models.ForeignKey(Weapon, on_delete=models.CASCADE)

class Enemy(Character):
    damage = models.IntegerField(default=50)