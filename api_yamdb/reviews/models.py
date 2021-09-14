import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256,
                            verbose_name='Наименование категории')
    slug = models.SlugField(unique=True,
                            verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(
        validators=[
            MaxValueValidator(datetime.date.today().year),
            MinValueValidator(0)
        ])
    description = models.TextField(blank=True)
    genre = models.ManyToManyField(Genre, related_name='genre')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='category'
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name

