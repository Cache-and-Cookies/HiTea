from django.contrib import admin
from django.urls import path
from . import views as menu_views

urlpatterns = [
    path('<str:model>', menu_views.getMenuData, name='menu'),
]