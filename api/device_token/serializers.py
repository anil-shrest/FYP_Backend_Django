from .models import DeviceToken
from rest_framework import serializers


# Device token serializer
class DeviceTokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeviceToken
        depth = 1
        fields = ['id', 'device_key']

    # def get_author_username(self, appointment):
    #     username = appointment.author.id
    #     return username
    
