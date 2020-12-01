from django.shortcuts import render
from .models import *


def menu(request):
    freshFruitProducts = FreshFruit.objects.all()
    milkTeaProducts = MilkTea.objects.all()
    lemonTeaProducts = LemonTea.objects.all()
    cheeseFoamProducts = CheeseFoam.objects.all()
    foodProducts = Food.objects.all()

    context = {
        'freshFruitProducts': freshFruitProducts,
        'milkTeaProducts': milkTeaProducts,
        'lemonTeaProducts': lemonTeaProducts,
        'cheeseFoamProducts': cheeseFoamProducts,
        'foodProducts': foodProducts,
    }

    return render(request, 'menu/menu.html', context)

