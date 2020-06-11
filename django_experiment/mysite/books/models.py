from django.db import models


class Book(models.Model):

    def __str__(self):
        return self.name + '-' + self.author + ' ' + self.type + ' ' + self.price

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=40)
    price = models.CharField(max_length=30)
    type = models.CharField(max_length=50)

