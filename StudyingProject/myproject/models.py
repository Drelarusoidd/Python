from django.db import models

# Create your models here.
class Customer(models.Model):
    
    email = models.CharField(max_length=256, blank=False)
    name = models.CharField(max_length=50, blank=False)
    interior = models.BooleanField(default=False)
    logo = models.BooleanField(default=False)
    graphic = models.BooleanField(default=False)