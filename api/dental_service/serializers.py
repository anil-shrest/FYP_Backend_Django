from rest_framework import serializers
from .models import Services
from doctors.serializers import DoctorPropertySerializer


# Servives serializer creation
class ServiceSerializer(serializers.ModelSerializer):

    service_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Services
        depth = 1
        fields = ['id', 'service_title',
                  'service_detail', 'service_image', 'doctor']

    def save(self):
        service = Services(
            service_title=self.validated_data['service_title'],
            service_detail=self.validated_data['service_detail'],
            service_image=self.validated_data['service_image'],
        )
        service.save()
        return service


# Service property serializer
class ServicePropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ['pk', 'service_title',
                  'service_detail', 'service_image']


# Doctor and service serializer 
class DoctorServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ('id', 'service_title', 'service_detail')
