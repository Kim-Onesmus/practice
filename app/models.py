from django.db import models

# Create your models here.

class Animal (models.Model):
    Animal_name = models.CharField(max_length=20)
    update = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    Img = models.ImageField()
    Description = models.TextField()
    Price_Ksh = models.IntegerField()
    Offer = models.BooleanField(default=False)

    def __str__(self):
        return self.Animal_name

class Customer (models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    password2 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

class Locate(models.Model):
    location = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"distance from {self.location} to {self.destination} is {self.distance} km"
