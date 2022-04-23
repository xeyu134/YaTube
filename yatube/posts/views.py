from django.http import HttpResponse
from django.shortcuts import render


# Главная страница.
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Страница постов группы.
def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template)
