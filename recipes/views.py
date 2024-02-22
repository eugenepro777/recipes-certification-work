from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Recipe
from .forms import RecipeForm
from django.shortcuts import render


def index(request):
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'home/index.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def recipe_list(request):
    recipes = get_list_or_404(Recipe)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # 1
            messages.success(request, 'Вы успешно зарегистрировались! Теперь вы можете войти.')
            request.session['show_registration_message'] = True
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})


def login(request):
    show_registration_message = request.session.pop('show_registration_message', False)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html',
                  {'form': form, 'show_registration_message': show_registration_message})


@login_required
def logout(request):
    return render(request, 'recipes/logout.html')


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})


@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe_id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form, 'recipe': recipe})
