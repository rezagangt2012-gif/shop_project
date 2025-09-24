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
    order = models.OneToOneField('Order' , models.CASCADE , related_name='Customer')


class Order(models.Model):
    total_price = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    priority = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    product = models.ManyToManyField(Product, through='OrderItem', related_name='orders')


class OrderItem(models.Model):
    name = models.CharField(max_length=200 , default='default_value')
    category = models.CharField(max_length=300 ,default='default_value' )
    price = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)



