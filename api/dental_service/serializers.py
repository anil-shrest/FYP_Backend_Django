from rest_framework import serializers
from .models import Services
from doctors.serializers import DoctorPropertySerializer
# from doctor.serializers import DoctoreSerializer


# Servives serializer creation
class ServiceSerializer(serializers.ModelSerializer):

    # doctor_data = DoctorPropertySerializer(many=True)
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


class DoctorServiceSerializer(serializers.ModelSerializer):
    # doctor = serializers.CharField(source='doctor')
    # doctor_data = DoctorPropertySerializer(many=True)

    class Meta:
        model = Services
        fields = ('id', 'service_title', 'service_detail')
