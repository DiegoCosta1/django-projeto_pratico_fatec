from os import truncate
from django.db import models
# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     firstname = models.CharField(max_length=32)
#     lastname = models.CharField(max_length=32)

class Album(models.Model):
    title = models.CharField(max_length=256)
    artist = models.CharField(max_length=256)
    art = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()

class Movie(models.Model):
    title = models.CharField(max_length=256)
    director = models.CharField(max_length=256)
    art = models.CharField(max_length=256)
    genre = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()