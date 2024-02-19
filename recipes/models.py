from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='images/', default='default_image.png', blank=True, verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True)
    recipes = models.ManyToManyField(Recipe)
