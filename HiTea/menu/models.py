from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from multiselectfield import MultiSelectField


# Create your models here.
class Topping(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=99, decimal_places=2)
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
    toppings = models.ManyToManyField(Topping)
    isHot = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.product.name


class MilkTea(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = models.ManyToManyField(Topping)
    isHot = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.product.name


class LemonTea(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = models.ManyToManyField(Topping)
    isHot = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.product.name


class CheeseFoam(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    toppings = models.ManyToManyField(Topping)
    isHot = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return self.product.name


class Food(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.product.name


