from django.urls import path, include
from . import views as store_views

urlpatterns = [
    path('', store_views.home, name='home'),
]
