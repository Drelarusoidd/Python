from django.db import models
from django.conf import settings

# Create your models here.
class Unit(models.Model):
    
    unit = models.CharField(max_length=200)

    @classmethod
    def create(self, unit):
        obj = self.objects.create(unit=unit)

        return obj

    def __str__(self):
        return self.unit


class Position(models.Model):
    position = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.position

class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    full_name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default='')
    department = models.ForeignKey(Unit, on_delete=models.CASCADE, default='')
    start_work = models.DateField()


class Employee(models.Model):
    
    full_name = models.CharField(max_length=100, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, default='')
    department = models.ForeignKey(Unit, on_delete=models.CASCADE, default='')
    start_work = models.DateField()