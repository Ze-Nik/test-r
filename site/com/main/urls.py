from django.urls import path, include
from . import views

urlpatterns = [
    path('titul_page', views.titul_page, name='Титульная страница'),
    path('user_page', views.user_page, name='Страница пользователя'),
    path('reg_page', views.reg_page, name='Страница регистрации'),
    path('auto_page', views.auto_page, name='Страница авторизации')
]
