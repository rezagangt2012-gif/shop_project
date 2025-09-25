from django.shortcuts import render , redirect
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Product , Order ,  Customer
from .serializers import ProductSerializer, OrderSerializer , CustomerSerializer
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


class CustomerMixinsApiView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request: Request, pk):
        return self.retrieve(request, pk)
    
def add_item_to_box(request, item_id):
    item = Product.objects.get(id=item_id)
    order_box, created = Order.objects.get_or_create(id=1)

    order_box.items.add(item)
    order_box.calculate_total_price()

    return redirect('order_box_detail')

def order_box_detail(request):
    order_box = Order.objects.get(id=1)
    return render(request, 'order_box/detail.html', {'order_box': order_box})
    

    
#endregion 