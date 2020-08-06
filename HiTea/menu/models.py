from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField

TOPPING_CHOICES = (
    ('Pearl ($0.50)', 'Pearl ($0.50)'),
    ('Red Beans ($0.50)', 'Red Beans ($0.50)'),
    ('Coconut Jelly ($0.50)', 'Coconut Jelly ($0.50)'),
    ('Pudding ($0.50)', 'Pudding ($0.50)'),
    ('Agar Ball ($0.75)', 'Agar Ball ($0.75)'),
    ('Aloe ($0.75)', 'Aloe ($0.75)'),
    ('Popping Boba ($0.75)', 'Popping Boba ($0.75)'),
    ('Oreo ($1.00)', 'Oreo ($1.00)'),
    ('Cheese Foam ($1.00)', 'Cheese Foam ($1.00)'),
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
    isHot = models.BooleanField(default=False, null=False, blank=False)

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


class MilkTea(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name


class LemonTea(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name


class CheeseFoam(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = MultiSelectField(max_choices=10, choices=TOPPING_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.product.name


class Food(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name
