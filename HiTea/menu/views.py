from django.shortcuts import render
from .models import *


def getMenuData(request):
    freshFruitProducts = FreshFruit.objects.all()
    hotMilkTeaProducts = HotMilkTea.objects.all()
    icedMilkTeaProducts = IcedMilkTea.objects.all()
    hotLemonTeaProducts = HotLemonTea.objects.all()
    icedLemonTeaProducts = IcedLemonTea.objects.all()
    hotCheeseFoamProducts = HotCheeseFoam.objects.all()
    icedCheeseFoamProducts = IcedCheeseFoam.objects.all()

    # 2) pack data into context:
    context = {
        'freshFruitProducts': freshFruitProducts,
        'hotMilkTeaProducts': hotMilkTeaProducts,
        'icedMilkTeaProducts': icedMilkTeaProducts,
        'hotLemonTeaProducts': hotLemonTeaProducts,
        'icedLemonTeaProducts': icedLemonTeaProducts,
        'hotCheeseFoamProducts': hotCheeseFoamProducts,
        'icedCheeseFoamProducts': icedCheeseFoamProducts,
    }

    # 3) render
    return render(request, 'menu/menu.html', context)

