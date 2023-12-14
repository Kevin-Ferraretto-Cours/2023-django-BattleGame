from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from math import ceil
from  django.utils import timezone
import random
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from characters.models import Enemy, Paladin, Archer, Barbarian, Magician
from game.models import Game
from tokens.models import Tokens

class chooseDificultyForm(forms.Form):
    CHOICES = [
        (1, 'Difficulté 1'), 
        (2, 'Difficulté 2'), 
        (3, 'Difficulté 3'), 
        (4, 'Difficulté 4'), 
        (5, 'Difficulté 5'), 
    ]
    chooseDificulty = forms.ChoiceField(choices = CHOICES)

def chooseMode(request):
    return render(request, "play.html")

def PvP(request):
    # Récupérer tout les identifiant des session active
    active_sessions = Session.objects.filter(expire_date__gte = timezone.now())
    user_ids = []
    
    # Récupere les identifiant d'utilisateur pour chaque session active
    for session in active_sessions:
        data = session.get_decoded()
        user_id = data.get('_auth_user_id', None)
        if user_id:
            user_ids.append(user_id)
    
    logged_in_users = User.objects.filter(id__in=user_ids)
    
    return render(request, "pvp.html", {'logged_in_users': logged_in_users})

def PvE(request):
    state = get_object_or_404(Game, idUser = request.user)
    if state.state == None:
        form = chooseDificultyForm()
        return render(request, "pve.html", {"form" : form})
    elif state.state == 1:
        context = {}
        enemy = get_object_or_404(Enemy, id = state.idEnemy)
        context['enemy'] = enemy
        context['state'] = state
        
        if state.typePersonnage == "Barbarian":
            character = Barbarian.objects.get(pk=state.idPersonnage)
            context['max_rage'] = character.getMaxRage()
        elif state.typePersonnage == "Archer":
            character = Archer.objects.get(pk=state.idPersonnage)
            context['max_mana'] = character.getMaxMana()
        elif state.typePersonnage == "Paladin":
            character = Paladin.objects.get(pk=state.idPersonnage)
            context['max_rage'] = character.getMaxRage()
        elif state.typePersonnage == "Magician":
            character = Magician.objects.get(pk=state.idPersonnage)
            context['max_mana'] = character.getMaxMana()
        
        context['character'] = character
        context['character_maxhp'] = character.getMaxHp()
        return render(request, "pve.html", context)
    elif state.state > 1 :
        return redirect('chooseMode')
    else:
        form = chooseDificultyForm()
        return render(request, "chooseDifficulty.html", {"form" : form})

def generateMonster(request):
    difficulty = int(request.POST["chooseDificulty"])
    enemy = Enemy.objects.order_by('?').first()
    if difficulty <= 1:
        enemy.hp = ceil((random.randrange(1,10*difficulty)/25) * enemy.hp)
    if difficulty == 2:
        enemy.hp = ceil((random.randrange(10,10*difficulty)/25) * enemy.hp)
    if difficulty == 3:
        enemy.hp = ceil((random.randrange(20,10*difficulty)/25) * enemy.hp)
    if difficulty == 4:
        enemy.hp = ceil((random.randrange(30,10*difficulty)/25) * enemy.hp)
    if difficulty >= 5:
        enemy.hp = ceil((random.randrange(40,10*difficulty)/25) * enemy.hp)
    
    state= get_object_or_404(Game, idUser = request.user)
    state.state = 1
    state.idEnemy = enemy.id
    state.enemyHp = enemy.hp
    state.enemyMaxHp = enemy.hp
    state.enemyDamage = enemy.damage
    
    state.save()
    return redirect('pve')

def tokenAttack(request):
    state = get_object_or_404(Game, idUser = request.user)
    historique = state.historique
    enemy = get_object_or_404(Enemy, id = state.idEnemy)
    if state.typePersonnage == "Barbarian":
        character = Barbarian.objects.get(pk=state.idPersonnage)
        for item in range(0, character.tokens_limit[1]):
            if use(state):
                if character.tokensAvailable == None:
                    character.tokensAvailable = 1
                else:
                    character.tokensAvailable += 1
    elif state.typePersonnage == "Archer":
        character = Archer.objects.get(pk=state.idPersonnage)
        for item in range(0, character.tokens_limit[0]):
            if use(state):
                if character.tokensAvailable == None:
                    character.tokensAvailable = 1
                else:
                    character.tokensAvailable += 1
    elif state.typePersonnage == "Paladin":
        character = Paladin.objects.get(pk=state.idPersonnage)
        for item in range(0, character.tokens_limit[1]):
            if use(state):
                if character.tokensAvailable == None:
                    character.tokensAvailable = 1
                else:
                    character.tokensAvailable += 1
    elif state.typePersonnage == "Magician":
        character = Magician.objects.get(pk=state.idPersonnage)
        for item in range(0, character.tokens_limit[0]):
            if use(state):
                if character.tokensAvailable == None:
                    character.tokensAvailable = 1
                else:
                    character.tokensAvailable += 1
    
    canUseOtherToken(character)
    
    # Si aucun Tokens n'est possitif le mob attack
    if  character.tokensAvailable == None:
        dmg = enemy.damage_reduction(enemy.has_crit(state.enemyDamage), character)
        if (character.hp - dmg) <= 0:
            character.hp = 0
            historique[len(historique)] = f"{enemy.name} à tué {character.name}"
            character.save()
        else:
            character.takeDamage(dmg)
            historique[len(historique)] = f"{enemy.name} à infligé {dmg} de dégats à {character.name}"
    
    
    
    state.save()
    character.save()
    return redirect('pve')

def use(state) -> bool:
    historique = state.historique
    rand = random.randint(0,100)
    if rand >= 50:
        historique[len(historique)] = "The token landed on the good side !"
        state.save()
        return True
    else:
        historique[len(historique)] = "The token landed on the bad side :("
        state.save()
        return False

def handAttack(request):
    state = get_object_or_404(Game, idUser = request.user)
    historique = state.historique
    if state.typePersonnage == "Barbarian":
        character = Barbarian.objects.get(pk=state.idPersonnage)
    elif state.typePersonnage == "Archer":
        character = Archer.objects.get(pk=state.idPersonnage)
    elif state.typePersonnage == "Paladin":
        character = Paladin.objects.get(pk=state.idPersonnage)
    elif state.typePersonnage == "Magician":
        character = Magician.objects.get(pk=state.idPersonnage)
    
    if state.state == 1:
        enemy = get_object_or_404(Enemy, id = state.idEnemy)
        dmg = character.damage_reduction(character.has_crit(character.getAttack()), enemy)
        if (state.enemyHp - dmg) <= 0:
            historique[len(historique)] = f"{character.name} à tué {enemy.name}"
            state.enemyHp = 0
        else:
            state.enemyHp = (state.enemyHp - dmg)
            historique[len(historique)] = f"{character.name} à infligé {dmg} de dégats à {enemy.name}"
            dmg = enemy.damage_reduction(enemy.has_crit(state.enemyDamage), character)
            if (character.hp - dmg) <= 0:
                character.hp = 0
                historique[len(historique)] = f"{enemy.name} à tué {character.name}"
                character.save()
            else:
                character.takeDamage(dmg)
                historique[len(historique)] = f"{enemy.name} à infligé {dmg} de dégats à {character.name}"
        state.save()
        
    return redirect('pve')

def clearGame(request):
    state = get_object_or_404(Game, idUser = request.user)
    state.state = 0
    state.idEnemy = None
    state.enemyHp = None
    state.enemyMaxHp = None
    state.enemyDamage = None
    state.historique = {}
    state.save()
    
    if state.typePersonnage == "Barbarian":
        character = Barbarian.objects.get(pk=state.idPersonnage)
    elif state.typePersonnage == "Archer":
        character = Archer.objects.get(pk=state.idPersonnage)
    elif state.typePersonnage == "Paladin":
        character = Paladin.objects.get(pk=state.idPersonnage)
    elif state.typePersonnage == "Magician":
        character = Magician.objects.get(pk=state.idPersonnage)
    
    if character.hp <= 0:
        character.full_heal()
        character.full_mana_rage()
    
    return redirect('chooseMode')

def useToken(request, tokenId):
    state = get_object_or_404(Game, idUser = request.user)
    token = get_object_or_404(Tokens, id = tokenId)
    enemy = get_object_or_404(Enemy, id = state.idEnemy)
    historique = state.historique
    if state.typePersonnage == "Barbarian":
        character = Barbarian.objects.get(pk=state.idPersonnage)
        character.rage -= token.cost
    elif state.typePersonnage == "Archer":
        character = Archer.objects.get(pk=state.idPersonnage)
        character.mana -= token.cost
    elif state.typePersonnage == "Paladin":
        character = Paladin.objects.get(pk=state.idPersonnage)
        character.rage -= token.cost
    elif state.typePersonnage == "Magician":
        character = Magician.objects.get(pk=state.idPersonnage)
        character.mana -= token.cost
    character.tokensAvailable -= 1
    
    dmg = character.damage_reduction(token.damage, enemy)
    if (state.enemyHp - dmg) <= 0:
        historique[len(historique)] = f"{character.name} à utiliser le token {token.name} est à tué {enemy.name}."
        state.enemyHp = 0
    else:
        historique[len(historique)] = f"{character.name} à utiliser le token {token.name} est à infliger {dmg} de dégats à {enemy.name}."
        state.enemyHp = (state.enemyHp - dmg)
    
    if character.tokensAvailable <= 0:
        character.tokensAvailable = None
        dmg = enemy.damage_reduction(enemy.has_crit(state.enemyDamage), character)
        if (character.hp - dmg) <= 0:
            character.hp = 0
            historique[len(historique)] = f"{enemy.name} à tué {character.name}"
            character.save()
        else:
            character.takeDamage(dmg)
            historique[len(historique)] = f"{enemy.name} à infligé {dmg} de dégats à {character.name}"
    else:
        canUseOtherToken(character)
    state.save()
    character.save()
    return redirect('pve')



def canUseOtherToken(character) -> None:
    can_use_token = False
    for t in character.tokens.values_list('id', flat=True):
        token = get_object_or_404(Tokens, id = t)
        if hasattr(character, 'mana'):
            if token.cost <= character.mana:
                can_use_token = True
        else:
            if token.cost <= character.rage:
                can_use_token = True
    if not can_use_token:
        character.tokensAvailable = None
        character.save()