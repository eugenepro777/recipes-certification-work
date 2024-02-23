from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=255, label='Имя пользователя')  # !
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Подтвердите пароль')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['confirm_password']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Данный email уже используется')
        return data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        mail = User.objects.exclude(id=self.instance.id).filter(email=data)
        if mail.exists():
            raise forms.ValidationError('Данный email уже используется')
        return data


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_birth', ]
