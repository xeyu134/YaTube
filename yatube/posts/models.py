from django.db import models
from django.contrib.auth import get_user_model  # Импортируем модель Users

# Create your models here.
User = get_user_model()


class Post(models.Model):
    # Тип TextField для хранения произвольного текста
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)  # Тип даты.
    author = models.ForeignKey(  # связь по ключу с классом Users.
        User,
        # При удалении объекта класса Users удаляются все его данные.
        on_delete=models.CASCADE,
        related_name='posts'
    )
