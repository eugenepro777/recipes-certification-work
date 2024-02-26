from django.urls import path, include

from .views import user_login, user_logout, registration, user_page

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', user_page, name='user_page'),
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
