from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

TOPPING_CHOICES = (
    ('a', 'Pearl ($0.50)'),
    ('b', 'Red Beans ($0.50)'),
    ('c', 'Coconut Jelly ($0.50)'),
    ('d', 'Pudding ($0.50)'),
    ('e', 'Agar Ball ($0.75)'),
    ('f', 'Aloe ($0.75)'),
    ('g', 'Popping Boba ($0.75)'),
    ('h', 'Oreo ($1.00)'),
    ('i', 'Cheese Foam ($1.00)'),
)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    image = models.ImageField(default='bbt.png', null=True, blank=True)
    calories = models.IntegerField(default=0, validators=[
        MaxValueValidator(999999),
        MinValueValidator(0),
    ])

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url




class FreshFruit(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name


class HotMilkTea(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name

class IcedMilkTea(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name


class HotLemonTea(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name


class IcedLemonTea(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name


class HotCheeseFoam(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name


class IcedCheeseFoam(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name
