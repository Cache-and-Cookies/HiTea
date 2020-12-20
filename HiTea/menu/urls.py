from django.urls import path
from . import views as menu_views

urlpatterns = [
    path('', menu_views.menu, name='menu-search'),
]