from django.http import HttpResponse

# Главная страница.
def index(request):
    return HttpResponse('Главная страница')


# Страница постов группы.
def group_posts(resuest, pk):
    return HttpResponse(f'Посты группы {pk}')
