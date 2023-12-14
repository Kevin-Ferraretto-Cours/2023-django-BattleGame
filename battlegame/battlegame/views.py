from django.shortcuts import render
from game.models import Game
from tokens.models import Tokens

def index(request):
    has_account = False
    if request.user.is_authenticated:
        for x in Game.objects.all():
            if x.idUser == request.user:
                has_account = True
    context = { "has_account" : has_account }
    return render(request, "home.html", context)

def createTokens(nom, dmg, cout):
    spell = Tokens(
        name = nom,
        damage = dmg,
        cost = cout,
    )
    spell.save()

def init(request):
    createTokens("Frappe écrasante", 30, 10)
    createTokens("Onde de choc", 45, 15)
    createTokens("Invocation de masse", 50, 20)
    createTokens("Furie", 35, 15)
    createTokens("Écrasement de terre", 65, 30)
    
    createTokens("Flèches de glace", 60, 20)
    createTokens("Pluie de feu", 100, 30)
    createTokens("Flèches de lumière", 75, 20)
    createTokens("Flèches de vent", 40, 10)
    createTokens("Flèches de poison", 45, 15)
    
    createTokens("Tourbillon", 25, 10)
    createTokens("Coup assomant", 30, 15)
    createTokens("Enrage", 50, 20)
    createTokens("Tourment", 35, 15)
    createTokens("Frappe fulgurante", 60, 25)

    createTokens("Boule de feu", 60, 20)
    createTokens("Rayon de glace", 60, 25)
    createTokens("Explosion magique", 75, 40)
    createTokens("Éclair", 40, 20)
    createTokens("Nova", 100, 50)
