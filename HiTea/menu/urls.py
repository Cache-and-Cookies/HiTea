from django.contrib import admin
from django.urls import path
from . import views as menu_views

urlpatterns = [
    path('', menu_views.getMenuData, name='menu-search'),
<<<<<<< HEAD
=======
    path('', menu_views.getMenuData, name='menu-home'),
>>>>>>> 4a96c8b74d3b0f1dc22875be455718a8c918e821
]