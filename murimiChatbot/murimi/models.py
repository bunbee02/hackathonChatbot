from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Province(models.Model):
    name = models.CharField(max_length=100)
    

class Practice(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    
 
    
class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class info(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    ph = models.IntegerField()
    rainfall = models.IntegerField()
    label = models.CharField(max_length=100)