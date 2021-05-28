from rest_framework import serializers
from .models import TimeTable
from account.models import NewUser


# Adding Appointment Serializer
class TimeTableSerializer(serializers.ModelSerializer):

    doctor_name = serializers.SerializerMethodField('get_doctor_username')
    staff = serializers.SerializerMethodField('get_author_user')

    class Meta:
        model = TimeTable
        depth = 1
        fields = [
            'id', 'time_space', 'doctor', 'author', 'doctor_name', 'staff'
        ]

    def get_doctor_username(self, time):
        doc_name = time.doctor.full_name
        return doc_name

    def get_author_user(self, author):
        name = author.author.id
        return name

# Time table serializer
class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = ['id', 'time_space', 'doctor']
