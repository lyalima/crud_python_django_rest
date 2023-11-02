from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.get_users, name='get_users'),
    path('get_user_by_nick/<str:nick>', views.get_user_by_nick, name='get_user_by_nick'),
    path('create_user/', views.create_user, name='create_user'),
    path('update_user/<str:nick>', views.update_user, name='update_user'),
    path('delete_user/<str:nick>', views.delete_user, name='delete_user'),
]