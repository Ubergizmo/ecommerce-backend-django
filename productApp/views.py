from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from productApp.models import Product,Category
from productApp.serializers import ProductSerializer, CategorySerializer
# Create your views here.
@csrf_exempt
def productApi(request, id=0):
    if request.method=='GET':
        if id == 0:
            product = Product.objects.all()
            product_serializer = ProductSerializer(product, many = True)
            return JsonResponse(product_serializer.data, safe = False,status=status.HTTP_200_OK)
        else :
            product = get_object_or_404(Product, pk=id)
            product_serializer = ProductSerializer(product)
            return JsonResponse(product_serializer.data, safe=False)
    elif request.method=='POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully", safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(product_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(productId = product_data['productId'])
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed to Update", safe = False)
    elif request.method=='DELETE':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return JsonResponse("Deleted Successfully", safe=False, status=status.HTTP_204_NO_CONTENT)
    

@csrf_exempt
def categoryApi(request, id=0):
    if request.method == 'GET':
        if id > 0:
            category = get_object_or_404(Category, pk=id)
            category_serializer = CategorySerializer(category)
            return JsonResponse(category_serializer.data, safe=False)
        else:
            categories = Category.objects.all()
            category_serializer = CategorySerializer(categories, many=True)
            return JsonResponse(category_serializer.data, safe=False)
    elif request.method == 'POST':
        category_data = JSONParser().parse(request)
        category_serializer = CategorySerializer(data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Category Added Successfully", safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(category_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        category_data = JSONParser().parse(request)
        category = Category.objects.get(categoryId = category_data['categoryId'])
        category_serializer = CategorySerializer(category, data=category_data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse("Category Updated Successfully", safe=False, status=status.HTTP_200_OK)
        return JsonResponse("Failed to Update", safe = False)
    elif request.method == 'DELETE':
        category = get_object_or_404(Category, pk=id)
        category.delete()
        return JsonResponse("Category Deleted Successfully", safe=False, status=status.HTTP_204_NO_CONTENT)

