from rest_framework import serializers
from .models import TimeTable
from account.models import NewUser
# from account.models import NewUser
# from doctors.serializers import DoctorSerializer


# Adding Appointment Serializer
class TimeTableSerializer(serializers.ModelSerializer):
    # author_data = AccountPropertySerializer()

    doctor_name = serializers.SerializerMethodField('get_doctor_username')
    staff = serializers.SerializerMethodField('get_author_user')
    # appointmentBy = serializers.SerializerMethodField('get_doc_name')
    # time_table = serializers.ListField(
    #     child=serializers.CharField(allow_blank=True))

    class Meta:
        model = TimeTable
        depth = 1
        fields = [
            'id', 'time_space', 'doctor', 'author', 'doctor_name', 'staff'
        ]
        # fields = ('__all__')

    def get_doctor_username(self, time):
        doc_name = time.doctor.full_name
        return doc_name

    def get_author_user(self, author):
        name = author.author.id
        return name


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = ['id', 'time_space', 'doctor']

# class UserSerializer(serializers.ModelSerializer):
#     time = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=TimeTable.objects.all())

#     class Meta:
#         model = NewUser
#         fields = ['id', 'username', 'appointment']