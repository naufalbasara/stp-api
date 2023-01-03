from django.urls import path
from . import views

urlpatterns = [
    # path('', views.api_home), #localhost:8000/api
    path('products/', views.ProductListCreateAPIView.as_view()), #list products api (get, create)
    path('products/<int:pk>/', views.ProductListCreateAPIView.as_view()), #detail product (get)
    path('products/<int:pk>/update', views.ProductDetailUpdateAPIView.as_view()), #update product (put)
    path('products/<int:pk>/delete', views.ProductDetailUpdateAPIView.as_view()), #delete product (destroy)
]