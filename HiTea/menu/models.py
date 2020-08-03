from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.DecimalField(max_digits=99, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    calories = models.IntegerField(max_length=10)

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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    TOPPING_CHOICES = (
        ('a', 'Pearl'),
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
    SUGAR_CHOICES = (
        ('a', 'No Sugar'),
        ('b', '30% Sugar'),
        ('c', '50% Sugar'),
        ('d', '80% Sugar'),
        ('e', '100% Sugar'),

    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)
    sugar = models.CharField(max_length=1, choices=SUGAR_CHOICES)


class IcedFreshFruit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    TOPPING_CHOICES = (
        ('a', 'Pearl'),
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
    SUGAR_CHOICES = (
        ('a', 'No Sugar'),
        ('b', '30% Sugar'),
        ('c', '50% Sugar'),
        ('d', '80% Sugar'),
        ('e', '100% Sugar'),

    )
    toppings = models.CharField(max_length=10, choices=TOPPING_CHOICES)
    sugar = models.CharField(max_length=5, choices=SUGAR_CHOICES)


class HotMilkTea(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    TOPPING_CHOICES = (
        ('a', 'Pearl'),
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
    SUGAR_CHOICES = (
        ('a', 'No Sugar'),
        ('b', '30% Sugar'),
        ('c', '50% Sugar'),
        ('d', '80% Sugar'),
        ('e', '100% Sugar'),

    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)
    sugar = models.CharField(max_length=1, choices=SUGAR_CHOICES)


class IcedMilkTea(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)
    TOPPING_CHOICES = (
        ('a', 'Pearl'),
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
    SUGAR_CHOICES = (
        ('a', 'No Sugar'),
        ('b', '30% Sugar'),
        ('c', '50% Sugar'),
        ('d', '80% Sugar'),
        ('e', '100% Sugar'),

    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)
    sugar = models.CharField(max_length=1, choices=SUGAR_CHOICES)


class HotLemonTea(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    TOPPING_CHOICES = (
        ('a', 'Pearl'),
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
    SUGAR_CHOICES = (
        ('a', 'No Sugar'),
        ('b', '30% Sugar'),
        ('c', '50% Sugar'),
        ('d', '80% Sugar'),
        ('e', '100% Sugar'),

    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)
    sugar = models.CharField(max_length=1, choices=SUGAR_CHOICES)


class IcedLemonTea(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    TOPPING_CHOICES = (
        ('a', 'Pearl'),
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
    SUGAR_CHOICES = (
        ('a', 'No Sugar'),
        ('b', '30% Sugar'),
        ('c', '50% Sugar'),
        ('d', '80% Sugar'),
        ('e', '100% Sugar'),

    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)
    sugar = models.CharField(max_length=1, choices=SUGAR_CHOICES)


class HotCheeseFoam(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    TOPPING_CHOICES = (
        ('a', 'Pearl'),
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
    SUGAR_CHOICES = (
        ('a', 'No Sugar'),
        ('b', '30% Sugar'),
        ('c', '50% Sugar'),
        ('d', '80% Sugar'),
        ('e', '100% Sugar'),

    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)
    sugar = models.CharField(max_length=1, choices=SUGAR_CHOICES)


class IcedCheeseFoam(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, )
    TOPPING_CHOICES = (
        ('a', 'Pearl'),
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
    SUGAR_CHOICES = (
        ('a', 'No Sugar'),
        ('b', '30% Sugar'),
        ('c', '50% Sugar'),
        ('d', '80% Sugar'),
        ('e', '100% Sugar'),

    )
    toppings = models.CharField(max_length=5, choices=TOPPING_CHOICES)
    sugar = models.CharField(max_length=1, choices=SUGAR_CHOICES)
