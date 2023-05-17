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
    
    
 
    
# class Crop(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()

class info(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()
    ph = models.IntegerField()
    rainfall = models.IntegerField()
    label = models.CharField(max_length=100)
    
    
class Disease(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No description')

    def __str__(self):
        return self.name

class Crop(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CropDisease(models.Model):
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='diseases', null=True)

    def __str__(self):
        return f"{self.crop} - {self.disease}"




    