from django.http import HttpResponse
from django.shortcuts import render

# Главная страница.
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Страница постов группы.
def group_posts(resuest, pk):
    return HttpResponse(f'Посты группы {pk}')
