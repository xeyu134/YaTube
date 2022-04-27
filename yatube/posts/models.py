from django.db import models
from django.contrib.auth import get_user_model  # Импортируем модель Users

# Create your models here.
User = get_user_model()


class Post(models.Model):
    text = models.TextField()  # Тип TextField для хранения произвольного текста
    pub_date = models.DateTimeField(auto_now_add=True)  # Тип даты.
    author = models.ForeignKey(  # связь по ключу с классом Users.
        User,
        on_delete=models.CASCADE,  # При удалении объекта класса Users удаляются все данные, связанные с ним.
        related_name='posts'
    )