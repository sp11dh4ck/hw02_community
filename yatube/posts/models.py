from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Уникальный адрес')
    description = models.TextField(verbose_name='Описание')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        verbose_name='Группа',
        blank=True,
        null=True,
        related_name='posts'
    )

    class Meta:
        verbose_name_plural = 'Посты'
        ordering = ('-pub_date',)
