from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Province(models.Province):
    name = models.CharField(max_length=100)
   
    
    
class Crop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class FarmingPractice(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    practice = models.TextField()