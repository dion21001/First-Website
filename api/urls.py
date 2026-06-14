from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='api-home'),
    path('coffees/', views.CoffeeProductListCreate.as_view(), name='coffee-list-create'),
    path('coffees/<int:pk>/', views.CoffeeProductRetrieveUpdate.as_view(), name='coffee-detail'),
    path('orders/', views.CoffeeOrderListCreate.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', views.CoffeeOrderRetrieveUpdate.as_view(), name='order-detail'),
]
