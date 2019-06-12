from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    imageUrl = models.CharField(max_length=1000)


class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    city = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    payment_data = models.CharField(max_length=100)
    items = models.TextField()
    fulfilled = models.BooleanField()

