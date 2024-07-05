from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from userApp.models import User
from userApp.serializers import UserSerializer
# Create your views here.
@csrf_exempt
def userApi(request, id=0):
    if request.method=='GET':
        if id == 0:
            user = User.objects.all()
            user_serializer = UserSerializer(user, many = True)
            return JsonResponse(user_serializer.data, safe = False,status=status.HTTP_200_OK)
        else :
            user = get_object_or_404(User, pk=id)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data, safe=False)
    elif request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(userId = user_data['userId'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed to Update", safe = False)
    elif request.method=='DELETE':
        user = get_object_or_404(User, pk=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False, status=status.HTTP_204_NO_CONTENT)
    
