from django.db import models
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=300 , default='default_value')
    price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    priority = models.IntegerField(default=0)


class Customer(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField(default='default_value')
    pnum = models.BigIntegerField(default=0)



class Order(models.Model):
    total_price = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    priority = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(Product, related_name='orders')

    def calculate_total_price(self):
        total = sum(item.price for item in self.items.all())
        self.total_price = total
        self.save()

