from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class HotFreshFruit(models.Model):
    pass


class IcedFreshFruit(models.Model):
    pass


class HotMilkTea(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    TOPPING_CHOICES = (
        ('a,', 'Pearl'),
        ('b', 'Grass Jelly'),
        ('c', 'Red Beans'),
        ('d', 'Coconut Jelly'),
        ('e', 'Pudding'),
        ('f', 'Agar Ball'),
        ('h', 'Aloe'),
        ('i', 'Popping Boba'),
        ('j', 'Oreo'),
        ('k', 'Cheese Foam'),
    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)


class IcedMilkTea(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    TOPPING_CHOICES = (
        ('a,', 'Pearl'),
        ('b', 'Grass Jelly'),
        ('c', 'Red Beans'),
        ('d', 'Coconut Jelly'),
        ('e', 'Pudding'),
        ('f', 'Agar Ball'),
        ('h', 'Aloe'),
        ('i', 'Popping Boba'),
        ('j', 'Oreo'),
        ('k', 'Cheese Foam'),
    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)


class HotLemonTea(models.Model):
    pass


class IcedLemonTea(models.Model):
    pass


class HotCheeseFoam(models.Model):
    pass


class IcedCheeseFoam(models.Model):
    pass
