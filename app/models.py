from django.db import models

class menu(models.Model):
    restaurant = models.CharField(max_length=50)
    food = models.CharField(max_length=50)
    photo = models.CharField(max_length=1000)
    votes= models.IntegerField()

class Article(models.Model):
    # id = models.CharField(max_length=100)
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

class phone(models.Model):
    name =  models.CharField(max_length=50)
    ph =  models.CharField(max_length=50)

class Point(models.Model):
    title = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()
