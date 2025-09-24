from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Product , Order , OrderItem , Customer
from .serializers import ProductSerializer, OrderSerializer , OrderItemSerializer , CustomerSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
#from django.contrib.auth import get_user_model


#region generic


class ProductGenericApiView(generics.ListCreateAPIView ) :
    queryset = Product.objects.order_by('priority').all()
    serializer_class = ProductSerializer

class ProductGenericDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.order_by('priority').all()
    serializer_class = ProductSerializer



class OrderGenericApiView(generics.ListCreateAPIView) :
    queryset = Order.objects.order_by('priority').all()
    serializer_class = OrderSerializer

class OrderMixinDetailApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Order.objects.order_by('priority').all()
    serializer_class = OrderSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request: Request, pk):
        return self.update(request, pk)
    
    def delete(self, request:Request, pk):
        return self.destroy(request, pk)
    
class OrderItemGenericApiView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemGenericDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer



class CustomerMixinsApiView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)
    
        print(Customer.objects.filter(order_id=some_order_id).values_list('order_id', flat=True))

        

        # بررسی وجود رکورد تکراری
        if Customer.objects.filter(order_id=some_order_id).exists():
             return Response({"error": "این سفارش قبلاً ثبت شده است."}, status=status.HTTP_400_BAD_REQUEST)
        


        else:
            new_customer = Customer(order_id=some_order_id, name=request.data.get('name'))
            new_customer.save()
            return Response({"success": "رکورد جدید ایجاد شد"}, status=status.HTTP_201_CREATED)





#endregion

