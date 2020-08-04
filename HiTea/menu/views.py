from django.shortcuts import render
from .models import *


def getMenuData(request):
    freshFruitProducts = freshFruit.objects.all()
    hotMilkTeaProducts = HotMilkTea.objects.all()
    icedMilkTeaProducts = IcedMilkTea.objects.all()
    hotLemonTeaProducts = HotLemonTea.objects.all()
    icedLemonTeaProducts = IcedLemonTea.objects.all()
    hotCheeseFoamProducts = HotCheeseFoam.objects.all()
    icedCheeseFoamProducts = IcedCheeseFoam.objects.all()

    # 2) pack data into context:
    context = {
        'hotFreshFruitProducts': hotFreshFruitProducts,
        'icedFreshFruitProducts': icedFreshFruitProducts,
        'hotMilkTeaProducts': hotMilkTeaProducts,
        'icedMilkTeaProducts': icedMilkTeaProducts,
        'hotLemonTeaProducts': hotLemonTeaProducts,
        'icedLemonTeaProducts': icedLemonTeaProducts,
        'hotCheeseFoamProducts': hotCheeseFoamProducts,
        'icedCheeseFoamProducts': icedCheeseFoamProducts,
    }

    # 3) render
    return render(request, 'menu/menu.html', context)

