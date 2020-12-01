from django.contrib import admin
from .models import *

admin.site.site_header = 'Hi Tea Admin Dashboard'

# @admin.register(Product)
class FoodAdmin(admin.ModelAdmin):

    class Meta:
        model = Product


admin.site.register(Product)
admin.site.register(Topping)
admin.site.register(FreshFruit, FoodAdmin)
admin.site.register(MilkTea, FoodAdmin)
admin.site.register(LemonTea, FoodAdmin)
admin.site.register(CheeseFoam, FoodAdmin)
admin.site.register(Food, FoodAdmin)
