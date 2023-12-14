from django.urls import path
from . import views

urlpatterns = [
    path('', views.chooseMode, name='chooseMode'),
    path('PvP', views.PvP, name='pvp'),
    path('PvE', views.PvE, name='pve'),
    path('Difficulty', views.generateMonster, name='generateMonster'),
    path('handAttack', views.handAttack, name='handAttack'),
    path('tokenAttack', views.tokenAttack, name='tokenAttack'),
    path('clearGame', views.clearGame, name='clearGame'),
    path('useToken/<int:tokenId>', views.useToken, name='useToken'),
]