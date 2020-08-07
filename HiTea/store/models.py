from django.db import models


# Create your models here.
class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=5000)
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name}\'s Message'