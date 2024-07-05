from django.urls import path
from adminApp import views

urlpatterns = [
    path('admins/', views.adminApi), 
    path('admins/<int:id>/', views.adminApi),
]
