from django.urls import path
from . import views


urlpatterns = [
    # path('', views.api_home), #localhost:8000/api
    path('register/', views.RegisterUser.as_view()),
    path('api/user/', views.UserAPIView.as_view()),
    path('products/', views.alt_product), #list products api (get, create)
    path('products/<int:pk>/', views.ProductDetailUpdateAPIView.as_view()), #detail product (get)
    path('products/<int:pk>/update', views.ProductDetailUpdateAPIView.as_view()), #update product (put)
    path('products/<int:pk>/delete', views.ProductDetailUpdateAPIView.as_view()), #delete product (destroy)
]