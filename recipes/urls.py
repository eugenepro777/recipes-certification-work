from django.urls import path

from .views import recipe_detail, recipe_list, category_list, category_recipes, add_recipe, edit_recipe


urlpatterns = [
    path('list/', recipe_list, name='recipe_list'),
    path('<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('edit/<int:recipe_id>', edit_recipe, name='edit_recipe'),
    path('add/', add_recipe, name='add_recipe'),
    path('category/list', category_list, name='category_list'),
    path('category/<int:category_id>', category_recipes, name='category_recipes'),
]
