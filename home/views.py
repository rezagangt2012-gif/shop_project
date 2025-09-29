from django.shortcuts import render , redirect
from django.http import Http404
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Product , Order ,  Customer
from .serializers import ProductSerializer, OrderSerializer , CustomerSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets
from . import urls
from django.utils import timezone

#from django.contrib.auth import get_user_model


#region generic


class ProductGenericApiView(generics.ListCreateAPIView ) :
    queryset = Product.objects.order_by('priority').all()
    serializer_class = ProductSerializer

class ProductGenericDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.order_by('priority').all()
    serializer_class = ProductSerializer



class OrderGenericApiView(generics.ListCreateAPIView) :
    serializer_class = OrderSerializer

    def get_queryset(self):
        if 'name' in self.kwargs:
            name = self.kwargs['name']
            try:
                customer = Customer.objects.get(name=name)
                return customer.orders.order_by('priority').all()
            except Customer.DoesNotExist:
                raise Http404("Customer not found")
        else:
            return Order.objects.order_by('priority').all()



class OrderMixinDetailApiView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Order.objects.order_by('priority').all()
    serializer_class = OrderSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request: Request, pk):
        return self.update(request, pk)
    
    def delete(self, request:Request, pk):
        return self.destroy(request, pk)
    



class CustomerGenericsApiView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerGenericsDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    
customer = Customer.objects.all() 


@api_view(["GET"])
def todays_orders(request):
    today = timezone.now().date()
    orders = Order.objects.filter(date=today)  
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
    
#endregion
