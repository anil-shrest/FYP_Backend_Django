from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Services
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .serializers import ServiceSerializer, ServicePropertySerializer, DoctorServiceSerializer
from rest_framework import permissions, status, generics, request, viewsets


# Service views creation

@api_view(['POST', ])
@parser_classes((MultiPartParser, ))
def service_view(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            service = serializer.save()
            data['response'] = "Services added successfully"
            data['service_title'] = service.service_title
            data['service_detail'] = service.service_detail
            # data['service_title'] = service.service_image
        else:
            data = serializer.errors
        return Response(data)

# View for service properties update


# @api_view(['PUT', ])
# @permission_classes((IsAuthenticated,))
# def service_update(request):
#     try:
#         user = request.user
#     except user.DoesNotExists:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "PUT":
#         serializer = ServicePropertySerializer(user, data=request.data)
#         data = {}
#         if serializer.is_valid():
#             serializer.save()
#             data['response'] = "Services updated"
#             return Response(data=data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To view all the service
class ServiceView(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Services.objects.select_related('doctor').all()
    # querset = Services.objects.filter(id=id)
    serializer_class = ServiceSerializer

    # To check the values
    # for project in queryset:
    #     print(project.doctor.full_name, project.service_title)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DoctorServiceView(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = DoctorServiceSerializer

    # def retrieve(self, request, *args, **kwargs):
    #     # The Primary Key of the object is passed to the retrieve method through self.kwargs
    #     object_id = self.kwargs['pk']


# # To edit service
# class ServiceEdit(generics.RetrieveUpdateDestroyAPIView):
#     # permission_classes = [permissions.IsAuthenticated]

#     queryset = Services.objects.all()
#     serializer_class = ServiceSerializer
