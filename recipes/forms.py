from django import forms

from .models import Recipe


class RecipeForm(forms.Form):
    title = forms.CharField(max_length=255, label='Название')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    cooking_steps = forms.CharField(widget=forms.Textarea, label='Шаги приготовления')
    cooking_time = forms.IntegerField(label='Время приготовления')
    image = forms.ImageField(label='Изображение блюда')
    ingredient_name_0 = forms.CharField(max_length=255, label='Название ингредиента')
    ingredient_quantity_0 = forms.CharField(max_length=255, label='Количество')

    def save(self):
        cleaned_data = self.cleaned_data
        product = Recipe.objects.create(
            name=cleaned_data['title'],
            description=cleaned_data['description'],
            cooking_steps=cleaned_data['cooking_steps'],
            cooking_time=cleaned_data['cooking_time'],
            image=cleaned_data['image'],
            ingredient_name_0=cleaned_data['ingredient_name_0'],
            ingredient_quantity_0=cleaned_data['ingredient_quantity_0']
        )
        return product


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=255, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
