from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заглавие')
    slug = models.SlugField(unique=True, verbose_name='Уникальный адрес')
    description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Группы'
        ordering = ['-title']


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Группа',
        related_name='posts'
    )

    class Meta:
        verbose_name_plural = 'Посты'
        ordering = ['-pub_date']
