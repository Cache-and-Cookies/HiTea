from django.shortcuts import render
from .models import *
from django.shortcuts import redirect


# Create your views here.
def home(request):
    return redirect('/menu/Hot-Fresh-Fruit/')


def getMenuData(request, product_type):
    # 1) look up product data in database:
    if product_type == 'Hot-Fresh-Fruit':
        products = HotFreshFruit.objects.all()  # specify query set here
    elif product_type == 'Iced-Fresh-Fruit':
        products = IcedFreshFruit.objects.all()
    elif product_type == 'Hot-Milk_Tea':
        products = HotMilkTea.objects.all()
    elif product_type == 'Iced-Milk-Tea':
        products = IcedMilkTea.objects.all()
    elif product_type == 'Hot-Lemon-Tea':
        products = HotLemonTea.objects.all()
    elif product_type == 'Iced-Lemon-Tea':
        products = IcedLemonTea.objects.all()
    elif product_type == 'Hot-Cheese-Foam':
        products = HotCheeseFoam.objects.all()
    elif product_type == 'Iced-Cheese-Foam':
        products = IcedCheeseFoam.objects.all()
    else:
        return redirect('/menu/Hot-Fresh-Fruit/')

    # 2) pack data into context:
    context = {
        'products': products,
    }

    # 3) render
    return render(request, 'menu/menu.html', context)

