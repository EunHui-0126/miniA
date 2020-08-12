from django.db import models

class menu(models.Model):
    restaurant = models.CharField(max_length=50)
    food = models.CharField(max_length=50)

class phone(models.Model):
    name =  models.CharField(max_length=50)
    ph =  models.CharField(max_length=50)
