from django.db import models
from brand.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    image = models.ImageField(upload_to='uploads/')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

class SoldCar(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    buyer = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{ self.car.name} {self.buyer.first_name}"
    

class Comment(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)