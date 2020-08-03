from django.shortcuts import render
from .models import *


# Create your views here.
def getMenuData(request, product_type):
    # 1) look up product data in database:
    if product_type == 'Hot-Fresh-Fruit':
        product_data = HotFreshFruit.objects.get()  # specify query set here
    elif product_type == 'Iced-Fresh-Fruit':
        product_data = IcedFreshFruit.objects.get()
    elif product_type == 'Hot-Milk_Tea':
        product_data = HotMilkTea.objects.get()
    elif product_type == 'Iced-Milk-Tea':
        product_data = IcedMilkTea.objects.get()
    elif product_type == 'Hot-Lemon-Tea':
        product_data = HotLemonTea.objects.get()
    elif product_type == 'Iced-Lemon-Tea':
        product_data = IcedLemonTea.objects.get()
    elif product_type == 'Hot-Cheese-Foam':
        product_data = HotCheeseFoam.objects.get()
    elif product_type == 'Iced-Cheese-Foam':
        product_data = IcedCheeseFoam.objects.get()
    else:
        return redirect()

    # 2) pack data into context:
    context = {

    }

    # 3) render template with context:
