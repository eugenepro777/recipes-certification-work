from django.urls import path

from .views import login, logout, recipe_detail, recipe_list, registration

app_name = 'recipes'

urlpatterns = [
    path('list/', recipe_list, name='recipe_list'),
    path('<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]