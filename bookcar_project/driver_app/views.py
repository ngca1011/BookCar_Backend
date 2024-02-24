from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Driver, Cab
from .serializers import DriverSerializer, CabSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET"])
def driver_list(request, format=None):

    if request.method == "GET":
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, many=True)
        return JsonResponse({"drivers": serializer.data}, safe=False)

@api_view(["GET", "PUT", "DELETE", "PATCH"])
def driver_detail(request, id, format=None):

    try:
        driver = Driver.objects.get(pk=id)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DriverSerializer(driver)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = DriverSerializer(driver, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PATCH":
        serializer = DriverSerializer(driver, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def cab_list(request, format=None):

    if request.method == "GET":
        cabs = Cab.objects.all()
        serializer = CabSerializer(cabs, many=True)
        return JsonResponse({"cabs": serializer.data}, safe=False)

@api_view(["GET", "PUT", "DELETE", "PATCH"])
def cab_detail(request, id, format=None):

    try:
        cab = Cab.objects.get(pk=id)
    except Cab.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CabSerializer(cab)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = CabSerializer(cab, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        cab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PATCH":
        serializer = CabSerializer(cab, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        