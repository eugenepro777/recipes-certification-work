from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.decorators import login_required

from .models import Recipe, Category
from .forms import RecipeForm


def index(request):
    categories = Category.objects.all()
    recipes = Recipe.objects.order_by('?')[:5]
    return render(request, 'home/index.html', {'categories': categories, 'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def category_recipes(request, category_id):
    recipes = Recipe.objects.filter(category_id=category_id)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'recipes/category_list.html', {'categories': categories})


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'recipes/category_list.html', {'category': category})


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html',
                  {'form': form})


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


# class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Recipe
#     success_url = reverse_lazy('recipes-home')
#
#     def test_func(self):
#         recipe = self.get_object()
#         return self.request.user == recipe.author
#
#
# class RecipeCreateView(LoginRequiredMixin, CreateView):
#     model = Recipe
#     fields = ['title', 'description', 'cooking_steps', 'cooking_time', 'image']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#
# class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Recipe
#     fields = ['title', 'description', 'cooking_steps', 'image']
#
#     def test_func(self):
#         recipe = self.get_object()
#         return self.request.user == recipe.author
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
