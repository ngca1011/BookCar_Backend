from rest_framework import serializers
from .models import Driver, Cab


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ["id", "name", "email", "phone_number", "created_at", "location"]


class CabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cab
        fields = ["id", "driver_id", "title", "type", "price_ratio"]
