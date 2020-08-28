from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField


# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=32, decimal_places=2)
    image = models.ImageField(default='bbt.png', null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=32, decimal_places=2)
    image = models.ImageField(default='bbt.png', null=True, blank=True)
    calories = models.IntegerField(default=0, validators=[
        MaxValueValidator(99999),
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

    @property
    def is_FreshFruit(self):
        return hasattr(self, "FreshFruit")

    @property
    def is_MilkTea(self):
        return hasattr(self, "MilkTea")

    @property
    def is_LemonTea(self):
        return hasattr(self, "LemonTea")

    @property
    def is_CheeseFoam(self):
        return hasattr(self, "CheeseFoam")

    @property
    def is_Food(self):
        return hasattr(self, "Food")


class FreshFruit(Product, models.Model):
    toppings = models.ManyToManyField(Topping, null=True)
    isHot = models.BooleanField(default=False, null=False, blank=False)


class MilkTea(Product, models.Model):
    toppings = models.ManyToManyField(Topping, null=True)
    isHot = models.BooleanField(default=False, null=False, blank=False)


class LemonTea(Product, models.Model):
    toppings = models.ManyToManyField(Topping, null=True)
    isHot = models.BooleanField(default=False, null=False, blank=False)


class CheeseFoam(Product, models.Model):
    toppings = models.ManyToManyField(Topping, null=True)
    isHot = models.BooleanField(default=False, null=False, blank=False)


class Food(Product, models.Model):
    description = models.CharField(max_length=1000, null=True)


