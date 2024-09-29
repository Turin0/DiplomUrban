from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def main_page(request):
    page_name = 'Новости игр'
    context = {
        'title': page_name,
        'page_name': page_name
    }
    return render(request, 'main.html', context)


def reviews(request):
    page_name = 'Обзоры игр'
    context = {
        'page_name': page_name,
        'title': page_name,
        'games': Game.objects.all(),
    }
    return render(request, 'reviews.html', context)


def game_page(request, game_id):
    page_name = 'Обзор'
    game = Game.objects.get(id=game_id)
    context = {
        'page_name': page_name,
        'title': page_name,
        'game': game
    }
    return render(request, 'game.html', context)



