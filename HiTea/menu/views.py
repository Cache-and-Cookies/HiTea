from django.shortcuts import render
from .models import *


def getMenuData(request):
    freshFruitProducts = FreshFruit.objects.all()
    milkTeaProducts = MilkTea.objects.all()
    lemonTeaProducts = LemonTea.objects.all()
    cheeseFoamProducts = CheeseFoam.objects.all()
    foodProducts = Food.objects.all()

    # 2) pack data into context:
    context = {
        'freshFruitProducts': freshFruitProducts,
        'milkTeaProducts': milkTeaProducts,
        'lemonTeaProducts': lemonTeaProducts,
        'cheeseFoamProducts': cheeseFoamProducts,
        'foodProducts': foodProducts,
    }

    # 3) render
    return render(request, 'menu/menu.html', context)

