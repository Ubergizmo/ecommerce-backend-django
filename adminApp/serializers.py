from rest_framework import serializers
from adminApp.models import Admin

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields=('adminId','username','password')