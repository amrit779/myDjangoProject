from django.db import models

# Create your models here.
class Students(models.Model):
    enrollmentNo = models.CharField(max_length=12)
    name = models.CharField(max_length=30)
    sign = models.CharField(max_length=20, default='')

class Order(models.Model):
    OrderDate = models.DateField()
    Region = models.CharField(max_length=10)
    Rep = models.CharField(max_length=10)
    Item = models.CharField(max_length=10)
    Units = models.IntegerField() 
    UnitCost = models.FloatField()
    Total = models.FloatField()
