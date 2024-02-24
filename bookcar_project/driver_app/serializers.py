from rest_framework import serializers
from .models import Driver, Cab

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'email', 'phone_number', 'created_at', 'latitude', 'longitude']

class CabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = ['id', 'driver_id', 'title', 'price_ratio']