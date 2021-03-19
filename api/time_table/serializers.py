from rest_framework import serializers
from .models import TimeTable
# from account.models import NewUser
from doctors.serializers import DoctorSerializer


# Adding Appointment Serializer
class TimeTableSerializer(serializers.ModelSerializer):
    # author_data = AccountPropertySerializer()

    doctor_name = serializers.SerializerMethodField('get_author_username')
    # appointmentBy = serializers.SerializerMethodField('get_doc_name')
    # time_table = serializers.ListField(
    #     child=serializers.CharField(allow_blank=True))

    class Meta:
        model = TimeTable
        # depth = 1
        fields = [
            'id', 'time_space', 'doctor_name'
        ]
        # fields = ('__all__')

    def get_author_username(self, doctor):
        username = doctor.doctor.full_name
        return username


# class DoctorSerializer(serializers.ModelSerializer):
#     doctor = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=TimeTable.objects.all())

#     class Meta:
#         model = Doctor
#         fields = ['id', 'username', 'appointment']
