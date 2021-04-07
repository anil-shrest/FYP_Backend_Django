from device_token.models import DeviceToken
from rest_framework import serializers


class DeviceTokenSerializer(serializers.ModelSerializer):
    # doctor = serializers.CharField(source='doctor')
    # doctor_data = DoctorPropertySerializer(many=True)
    # authors = serializers.SerializerMethodField('get_author_username')
    # doctor = serializers.SerializerMethodField('get_author_doctorname')

    class Meta:
        model = DeviceToken
        depth = 1
        fields = ['id', 'device_key']

    # def get_author_username(self, appointment):
    #     username = appointment.author.id
    #     return username
