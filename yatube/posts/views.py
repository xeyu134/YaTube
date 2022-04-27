from django.shortcuts import render
# Импортируем модель, чтобы обратиться к ней
from .models import Post


# Главная страница.
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию (от больших значений к меньшим)
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


# Страница постов группы.
def group_list(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)
