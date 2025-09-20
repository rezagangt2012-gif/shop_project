from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderItem, Product

@receiver(post_save, sender=OrderItem)
def reduce_inventory(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        product.inventory -= instance.quantity
        if product.inventory < 0:
            product.inventory = 0  # جلوگیری از منفی شدن موجودی
        product.save()
