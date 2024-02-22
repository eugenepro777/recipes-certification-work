from django.db import models
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название')
    quantity = models.CharField(max_length=80, verbose_name='Количество')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'ingredient'
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=120, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    # recipes = models.ManyToManyField(Recipe)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание')
    cooking_steps = models.TextField(verbose_name='Шаг приготовления')
    cooking_time = models.PositiveSmallIntegerField(default=0, verbose_name='Время приготовления')
    image = models.ImageField(upload_to='images/', default='default_image.png', blank=True, verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipe', verbose_name='Ингредиенты')
    # category = models.ManyToManyField(Category, through='RecipeCategory')
    category = models.ManyToManyField(Category, through='RecipeCategory')

    def __str__(self):
        return self.title


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'category')

    def __str__(self):
        return f'{self.recipe.title} - {self.category.name}'
