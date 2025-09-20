from django.urls import path, include
from .  import views 

urlpatterns = [
    path('product/generics/', views.ProductGenericApiView.as_view()),
    path('product/generics/<pk>', views.ProductGenericDetailApiView.as_view()),
    path('Order/generics/', views.OrderGenericApiView.as_view()),
    path('Order/mixins/<pk>', views.OrderMixinDetailApiView.as_view()), 
    path('OrderItem/generics/', views.OrderItemGenericApiView.as_view()),
    path('OrderItem/generics/<pk>', views.OrderItemGenericDetailApiView.as_view()),
]