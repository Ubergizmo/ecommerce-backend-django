from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from adminApp.models import Admin
from adminApp.serializers import AdminSerializer
# Create your views here.
@csrf_exempt
def adminApi(request, id=0):
    if request.method=='GET':
        if id == 0:
            admin = Admin.objects.all()
            admin_serializer = AdminSerializer(admin, many = True)
            return JsonResponse(admin_serializer.data, safe = False,status=status.HTTP_200_OK)
        else :
            admin = get_object_or_404(Admin, pk=id)
            admin_serializer = AdminSerializer(admin)
            return JsonResponse(admin_serializer.data, safe=False)
    elif request.method=='POST':
        admin_data = JSONParser().parse(request)
        admin_serializer = AdminSerializer(data=admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Added Successfully", safe=False, status=status.HTTP_201_CREATED)
        return JsonResponse(admin_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PUT':
        admin_data = JSONParser().parse(request)
        admin = Admin.objects.get(adminId = admin_data['adminId'])
        admin_serializer = AdminSerializer(admin, data=admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed to Update", safe = False)
    elif request.method=='DELETE':
        admin = get_object_or_404(Admin, pk=id)
        admin.delete()
        return JsonResponse("Deleted Successfully", safe=False, status=status.HTTP_204_NO_CONTENT)
    
