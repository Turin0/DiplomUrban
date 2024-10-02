from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.


def main_page(request):
    page_name = 'Новости игр'
    context = {
        'title': page_name,
        'page_name': page_name,
        'posts': Post.objects.all()
    }
    return render(request, 'main.html', context)


def post_add(request):
    page_name = 'Добавление поста'
    context = {
        'title': page_name,
        'page_name': page_name
    }
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        reviews = request.POST.get('reviews')
        Post.objects.create(title=title, description=description, reviews=reviews)
        return render(request, 'success.html')
    return render(request, 'post_add.html', context)


def show_reviews(request):
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



