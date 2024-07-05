from django.urls import path
from productApp import views

urlpatterns = [
    path('products/', views.productApi),       
    path('products/<int:id>/', views.productApi),
]
