from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.createCharacter, name='createCharacter'),
    path('inventory/', views.inventory, name='inventory'),
]