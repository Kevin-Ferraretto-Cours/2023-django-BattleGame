from django.shortcuts import render, redirect, get_object_or_404

from django import forms
from characters.models import Character, Paladin, Archer, Barbarian, Magician
from armor.models import Helmet, Chestplate, Leggings, Boots
from weapon.models import Weapon
from game.models import Game
from tokens.models import Tokens


class creationCharaterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ["helmet", "chestplate", "leggings", "boots", "weapon"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['helmet'].queryset = Helmet.objects.filter(starter = 1)
        self.fields['chestplate'].queryset = Chestplate.objects.filter(starter = 1)
        self.fields['leggings'].queryset = Leggings.objects.filter(starter = 1)
        self.fields['boots'].queryset = Boots.objects.filter(starter = 1)
        self.fields['weapon'].queryset = Weapon.objects.filter(starter = 1)

class creationCharaterTypeForm(forms.Form):
    typeCharacter = forms.ChoiceField(choices = [(c, c) for c in Character.TypeChoiceCharacter if c != "Monster"])


def createCharacter(request):
    if request.POST.get('weapon'):
        if request.method == 'POST':
            form = creationCharaterForm(request.POST)
            if form.is_valid():
                if request.POST["typeCharacter"] == "Paladin":
                    spell1 = Tokens.objects.get(name="Frappe écrasante")
                    spell2 = Tokens.objects.get(name="Onde de choc")
                    spell3 = Tokens.objects.get(name="Invocation de masse")
                    spell4 = Tokens.objects.get(name="Furie")
                    spell5 = Tokens.objects.get(name="Écrasement de terre")
                    new_character = Paladin(
                        name = request.user.username,
                        hp=request.POST["hp"],
                        defense=request.POST["defense"],
                        helmet=Helmet.objects.get(id=request.POST["helmet"]),
                        chestplate=Chestplate.objects.get(id=request.POST["chestplate"]),
                        leggings=Leggings.objects.get(id=request.POST["leggings"]),
                        boots=Boots.objects.get(id=request.POST["boots"]),
                        weapon=Weapon.objects.get(id=request.POST["weapon"]),
                        shield=Weapon.objects.get(id=request.POST["shield"]),
                        state=request.POST["state"],
                        typeCharacter=request.POST["typeCharacter"],
                    )
                    new_character.save()
                    new_character.tokens.add(spell1, spell2, spell3, spell4, spell5)
                    newGame = Game(
                        idUser = request.user,
                        typePersonnage = Character.TypeChoiceCharacter.Paladin,
                        idPersonnage = new_character.id,
                    )
                    newGame.save()
                    character = Paladin.objects.get(id=new_character.id)
                    character.full_heal()
                    character.full_mana_rage()
                elif request.POST["typeCharacter"] == "Archer":
                    spell1 = Tokens.objects.get(name="Flèches de glace")
                    spell2 = Tokens.objects.get(name="Pluie de feu")
                    spell3 = Tokens.objects.get(name="Flèches de lumière")
                    spell4 = Tokens.objects.get(name="Flèches de vent")
                    spell5 = Tokens.objects.get(name="Flèches de poison")
                    new_character = Archer(
                        name = request.user.username,
                        hp=request.POST["hp"],
                        defense=request.POST["defense"],
                        helmet=Helmet.objects.get(id=request.POST["helmet"]),
                        chestplate=Chestplate.objects.get(id=request.POST["chestplate"]),
                        leggings=Leggings.objects.get(id=request.POST["leggings"]),
                        boots=Boots.objects.get(id=request.POST["boots"]),
                        weapon=Weapon.objects.get(id=request.POST["weapon"]),
                        state=request.POST["state"],
                        typeCharacter=request.POST["typeCharacter"],
                    )
                    new_character.save()
                    new_character.tokens.add(spell1, spell2, spell3, spell4, spell5)
                    newGame = Game(
                        idUser = request.user,
                        typePersonnage = Character.TypeChoiceCharacter.Archer,
                        idPersonnage = new_character.id,
                    )
                    newGame.save()
                    character = Archer.objects.get(pk=new_character.id)
                    character.full_heal()
                    character.full_mana_rage()
                elif request.POST["typeCharacter"] == "Barbarian":
                    spell1 = Tokens.objects.get(name="Tourbillon")
                    spell2 = Tokens.objects.get(name="Coup assomant")
                    spell3 = Tokens.objects.get(name="Enrage")
                    spell4 = Tokens.objects.get(name="Tourment")
                    spell5 = Tokens.objects.get(name="Frappe fulgurante")
                    new_character = Barbarian(
                        name = request.user.username,
                        hp=request.POST["hp"],
                        defense=request.POST["defense"],
                        helmet=Helmet.objects.get(id=request.POST["helmet"]),
                        chestplate=Chestplate.objects.get(id=request.POST["chestplate"]),
                        leggings=Leggings.objects.get(id=request.POST["leggings"]),
                        boots=Boots.objects.get(id=request.POST["boots"]),
                        weapon=Weapon.objects.get(id=request.POST["weapon"]),
                        state=request.POST["state"],
                        typeCharacter=request.POST["typeCharacter"],
                    )
                    new_character.save()
                    new_character.tokens.add(spell1, spell2, spell3, spell4, spell5)
                    newGame = Game(
                        idUser = request.user,
                        typePersonnage = Character.TypeChoiceCharacter.Barbarian,
                        idPersonnage = new_character.id,
                    )
                    newGame.save()
                    character = Barbarian.objects.get(pk=new_character.id)
                    character.full_heal()
                    character.full_mana_rage()
                else:
                    spell1 = Tokens.objects.get(name="Boule de feu")
                    spell2 = Tokens.objects.get(name="Rayon de glace")
                    spell3 = Tokens.objects.get(name="Explosion magique")
                    spell4 = Tokens.objects.get(name="Éclair")
                    spell5 = Tokens.objects.get(name="Nova")
                    new_character = Magician(
                        name = request.user.username,
                        hp=request.POST["hp"],
                        defense=request.POST["defense"],
                        helmet=Helmet.objects.get(id=request.POST["helmet"]),
                        chestplate=Chestplate.objects.get(id=request.POST["chestplate"]),
                        leggings=Leggings.objects.get(id=request.POST["leggings"]),
                        boots=Boots.objects.get(id=request.POST["boots"]),
                        weapon=Weapon.objects.get(id=request.POST["weapon"]),
                        state=request.POST["state"],
                        typeCharacter=request.POST["typeCharacter"],
                    )
                    new_character.save()
                    new_character.tokens.add(spell1, spell2, spell3, spell4, spell5)
                    newGame = Game(
                        idUser = request.user,
                        typePersonnage = Character.TypeChoiceCharacter.Magician,
                        idPersonnage = new_character.id,
                    )
                    newGame.save()
                    character = Magician.objects.get(pk=new_character.id)
                    character.full_heal()
                    character.full_mana_rage()
                return redirect('home')
    elif request.POST.get('typeCharacter'):
        form = creationCharaterForm()
        form.fields['typeCharacter'] = forms.CharField(widget=forms.HiddenInput(attrs={'value': request.POST["typeCharacter"]}))
        form.fields['state'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 0}))
        weaponType = ""
        if request.POST["typeCharacter"] == "Archer":
            form.fields['hp'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 200}))
            form.fields['defense'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 50}))
            form.fields['mana'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 100}))
            weaponType = "Bow"
        elif request.POST["typeCharacter"] == "Magician":
            form.fields['hp'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 200}))
            form.fields['defense'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 50}))
            form.fields['mana'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 100}))
            weaponType = "Staff"
        elif request.POST["typeCharacter"] == "Barbarian":
            form.fields['hp'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 300}))
            form.fields['defense'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 25}))
            form.fields['rage'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 100}))
            weaponType = "Hatchet"
        elif request.POST["typeCharacter"] == "Paladin":
            form.fields['hp'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 200}))
            form.fields['defense'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 100}))
            form.fields['rage'] = forms.IntegerField(widget=forms.HiddenInput(attrs={'value': 50}))
            weaponType = "Mass"
            form.fields['shield'] = forms.ModelChoiceField(queryset=Weapon.objects.filter(type="Shield"))
        form.fields['weapon'].queryset = Weapon.objects.filter(type = weaponType)
        return render(request, "createCharacter.html", {"form" : form})
    else:
        form = creationCharaterTypeForm()
        return render(request, "createCharacter.html", {"form" : form})

def inventory(request):
    context = {}
    character = get_object_or_404(Game, idUser = request.user)
    if character.typePersonnage == "Barbarian":
        character = Barbarian.objects.get(pk=character.idPersonnage)
    elif character.typePersonnage == "Archer":
        character = Archer.objects.get(pk=character.idPersonnage)
    elif character.typePersonnage == "Paladin":
        character = Paladin.objects.get(pk=character.idPersonnage)
    elif character.typePersonnage == "Magician":
        character = Magician.objects.get(pk=character.idPersonnage)
    context['character'] = character
    
    context['maxhp'] = character.getMaxHp()
    context['defense'] = character.get_defense()
    context['crit_rate'] = character.get_crit_rate()
    context['crit_dmg'] = character.get_crit_dmg()
    return render(request, "inventory.html", context)
