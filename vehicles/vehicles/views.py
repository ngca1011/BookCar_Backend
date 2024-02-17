from django.http import JsonResponse
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def vehicle_list(request, format=None):

    if request.method == "GET":
        vehices = Vehicle.objects.all()
        serializer = VehicleSerializer(vehices, many=True)
        return JsonResponse({"vehicles": serializer.data}, safe=False)

    if request.method == "POST":
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def vehicle_detail(request, id, format=None):

    try:
        vehicle = Vehicle.objects.get(pk=id)
    except Vehicle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = VehicleSerializer(vehicle, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
