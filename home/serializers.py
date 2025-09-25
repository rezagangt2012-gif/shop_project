from rest_framework import serializers 
from .models import Customer , Product , Order, OrderItem



#from django.contrib.auth import get_user_model
#User = get_user_model()



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'



    def validate_order_id(self, value):
        if Customer.objects.filter(order_id=value).exists():
            raise serializers.ValidationError('this order has been detected')
        return value


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


