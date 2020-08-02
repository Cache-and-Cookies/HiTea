from django.urls import path, include
from . import views as user_views

urlpatterns = [
    path('', user_views.home, name='home')
]
