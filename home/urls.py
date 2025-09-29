from django.urls import path, include
from .  import views 

urlpatterns = [
    path('product/', views.ProductGenericApiView.as_view()),
    path('product/<pk>', views.ProductGenericDetailApiView.as_view()),
    path('Order/', views.OrderGenericApiView.as_view()),
    path('Order/<str:name>', views.OrderGenericApiView.as_view()),
    path('Customer/' , views.CustomerGenericsApiView.as_view()),
    path("orders/today/", views.todays_orders, name="todays_orders"),
    path("most/ordered/", views.most_ordered_things, name="most_ordred")
]