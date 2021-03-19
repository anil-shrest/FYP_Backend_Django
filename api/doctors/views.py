from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Doctor
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import DoctorSerializer, DoctorPropertySerializer
from rest_framework import permissions, status, generics, request, viewsets


# Doctor views creation
@api_view(['POST', ])
@parser_classes((MultiPartParser, ))
def doctor_view(request):
    if request.method == 'POST':
        serializer = DoctoreSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            doctor = serializer.save()
            data['response'] = "Doctor registered successfully"
            data['full_name'] = doctor.full_name
            data['nmc_number'] = doctor.nmc_number
            data['doc_type'] = doctor.doc_type
            data['speciality'] = doctor.speciality
        else:
            data = serializer.errors
        return Response(data)


# To view all the doctors
class DoctorView(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
