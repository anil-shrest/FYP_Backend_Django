from rest_framework import serializers
from .models import Doctor


# Doctor serializer creation
class DoctorSerializer(serializers.ModelSerializer):

    photo = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Doctor
        depth = 1
        fields = ['id', 'full_name', 'nmc_number',
                  'doc_type', 'speciality', 'photo']

    def save(self):
        doctor = Doctor(
            full_name=self.validated_data['full_name'],
            nmc_number=self.validated_data['nmc_number'],
            doc_type=self.validated_data['doc_type'],
            speciality=self.validated_data['speciality'],
            photo=self.validated_data['photo'],
        )
        doctor.save()
        return doctor


# Service property serializer
class DoctorPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['id', 'full_name', 'nmc_number',
                  'doc_type', 'speciality', 'photo']
