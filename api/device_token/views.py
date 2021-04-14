from django.shortcuts import render
from account.models import NewUser
from device_token.serializers import DeviceTokenSerializer
from requests.models import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from device_token import models
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_device_key(request):
    # related_doctor = Doctor.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        serializer = DeviceTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_device_key(request, author_id):
    # related_doctor = Doctor.objects.get(id=id)
    queryset = models.DeviceToken.objects.get(author=author_id)
    user = request.user
    if request.method == 'PUT':
        serializer = DeviceTokenSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save(author=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
