from django.db import models

# Create your models here.
from django.db import models

class SolarPanel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    solar_panel = models.ForeignKey(SolarPanel, on_delete=models.CASCADE)






    