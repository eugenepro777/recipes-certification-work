import csv
from django.contrib import admin
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from .models import Recipe, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name']
    list_filter = ['name']


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Для списка рецептов"""
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['display_id', 'title', 'category', 'cooking_time', 'author']
    list_filter = ['ingredients', 'cooking_time']
    readonly_fields = ['preview']
    search_fields = ['description']
    search_help_text = 'Поиск рецепта по описанию'
    actions = ['export_to_csv']
    """Для отдельного рецепта"""
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['title', 'slug']
            }
        ),
        (
            'Описание рецепта',
            {
                'description': 'Подробная информация о рецепте',
                'fields': ['description', 'cooking_steps', 'cooking_time'],
            }
        ),
        (
            'Ингредиенты',
            {
                'description': 'Ингредиенты для приготовления',
                'fields': ['ingredients'],
            }
        ),
        (
            'Загрузка изображения',
            {
                'description': 'Добавьте изображение для рецепта',
                'fields': ['image'],
            }
        ),
        (
            'Превью рецепта',
            {
                'fields': ['preview'],
            }
        ),
        (
            'Прочее',
            {
                'classes': ['collapse'],
                'description': 'Категория и автор',
                'fields': ['category', 'author'],
            }
        ),
    ]

    def display_id(self, obj):
        return f"Рецепт №{obj.id}"

    display_id.short_description = 'Рецепт'

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="width: 200px; height: auto;" alt="Изображения нет">')

    preview.short_description = 'Фото'

    @admin.action(description='Экспорт в CSV')
    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="recipe.csv"'
        writer = csv.writer(response)
        writer.writerow(['Номер', 'Название', 'Описание', 'Шаги приготовления', 'Ингредиенты', 'Категория', 'Время приготовления'])

        for recipe in queryset:
            writer.writerow(
                [recipe.id,
                 recipe.title,
                 recipe.description,
                 recipe.cooking_steps,
                 recipe.ingredients,
                 recipe.category,
                 recipe.cooking_time]
            )
        return response
