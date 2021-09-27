from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Country12(models.Model):
    country1 = models.CharField(max_length=40)

    def __str__(self):
        return self.country1

class City12(models.Model):
    city1 = models.CharField(max_length=40)

    def __str__(self) :
        return self.city1


class Order(models.Model):
    # Customer_ID = models.IntegerField(default=0)
    Transdate = models.CharField(max_length=100)
    Cfname = models.CharField(max_length=100)
    Clname = models.CharField(max_length=100)
    Country = models.ForeignKey(Country12,on_delete=models.CASCADE)
    Ccity = models.ForeignKey(City12,on_delete=models.CASCADE)
    Ptype = models.CharField(max_length=100)
    Product = models.CharField(max_length=40)
    Qty = models.IntegerField(default=0)
    Amount = models.IntegerField(default=0)
    Active = models.BooleanField()