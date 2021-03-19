from rest_framework import serializers
from .models import AppointmentTable
from account.models import NewUser
from account.serializers import AccountPropertySerializer


# Adding Appointment Serializer
class AppointmentSerializer(serializers.ModelSerializer):
    # author_data = AccountPropertySerializer()

    username = serializers.SerializerMethodField('get_author_username')
    doctor = serializers.SerializerMethodField('get_author_doctorname')

    class Meta:
        model = AppointmentTable
        depth = 1
        fields = [
            'id', 'appointmentBy', 'appointmentTime', 'username', 'doctor'
        ]
        # fields = ('__all__')

    def get_author_username(self, appointment):
        username = appointment.author.username
        return username

    def get_author_doctorname(self, doctor):
        doc_name = doctor.appointmentBy.full_name
        return doc_name


class UserSerializer(serializers.ModelSerializer):
    appointment = serializers.PrimaryKeyRelatedField(
        many=True, queryset=AppointmentTable.objects.all())

    class Meta:
        model = NewUser
        fields = ['id', 'username', 'appointment']
