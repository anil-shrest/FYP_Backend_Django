from django.shortcuts import get_object_or_404, render
from .models import AppointmentTable
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status, generics, request, viewsets
from account.models import NewUser
from .serializers import UserSerializer
from doctors.models import Doctor
from requests.models import Response
from rest_framework.response import Response
from rest_framework.views import APIView
from pyfcm import FCMNotification
from rest_framework.decorators import api_view, permission_classes
# from django.http import request
from device_token import models
User = NewUser


# TO book a new appointment
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def book_appointments(request, id):
    related_doctor = Doctor.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(appointmentBy=related_doctor, author=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


# To view all the available appointments
class AppointmentView(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = AppointmentTable.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.NewUser)


# To view specific user appointment
class AppointmentList(generics.ListCreateAPIView):
    # List all appointments, or create a new one.
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [permissions.IsAdminUser]
    # queryset = AppointmentTable.objects.all()
    # queryset = AppointmentTable.objects.filter(
    #     author=request)
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = AppointmentTable.objects.all()
        if user is not None:
            queryset = queryset.filter(author=user.id)
        return queryset

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class AppointmentEdit(generics.RetrieveUpdateDestroyAPIView):
    # Retrieve, update or delete a appointment instance.
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = AppointmentTable.objects.all()
    serializer_class = AppointmentSerializer


# To get, patch and delete respective appointment
class AppointmentDetailView(APIView):

    def get(self, request, *args, **kwargs):
        question = get_object_or_404(AppointmentTable, pk=kwargs['id'])
        serializer = AppointmentSerializer(question)
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        question = get_object_or_404(AppointmentTable, pk=kwargs['id'])
        serializer = AppointmentSerializer(
            question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(AppointmentSerializer(question).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        question = get_object_or_404(AppointmentTable, pk=kwargs['id'])
        question.delete()
        return Response("Appointment deleted", status=status.HTTP_204_NO_CONTENT)


# FCM declartion
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def appoint_confirm_fcm(request):
    related_doctor = Doctor.objects.get(id=id)
    user = request.user
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(appointmentBy=related_doctor, author=user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To send notfication to the staff - confirm appointment
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def sending_notification(request, staff_id):
    queryset = models.DeviceToken.objects.get(author=staff_id)
    # queryset = AppointmentTable.objects.get(id=staff_id).update(isBooked=True)
    # author = queryset.author
    # device_tokey = models.DeviceToken.objects.get(author=author)
    # device_token = device_tokey.device_key
    device_token = queryset.device_key
    print(device_token)
    fcm_servive = FCMNotification(
        api_key="AAAA0lFXPkM:APA91bFp1D6Ghp0n59_T5uRzbJQsmv8IaomrWKrbNuaAWVKUYtbULiiAY-NFMHKMZvdPf71AqRECufbypGz86RaTAhz4fbm_OnG31Rfq2ZYAhiH0rkM_D_Dyuue2dUR729Hh1E7hgBtS")
    message_title = "Appointment Booking Request"
    message_body = "A patient has booked an appointment"
    # click_action = "FLUTTER_NOTIFICATION_CLICK"
    device_key = device_token
    result = fcm_servive.notify_single_device(registration_id=device_key,
                                              message_body=message_body, message_title=message_title)
    return Response(result, status=status.HTTP_200_OK)


# To send notfication to the patient - confirmed appointment
@api_view(['POST'])
@permission_classes([])
def sending_confirmation_notification(request, appointment_id):
    queryset = AppointmentTable.objects.filter(
        id=appointment_id).update(is_booked=True)
    queryid = AppointmentTable.objects.get(id=appointment_id)
    print(queryid)
    patient = queryid.author
    device_id = models.DeviceToken.objects.get(author=patient)
    device_token = device_id.device_key
    print(device_token)
    # return Response(status=status.HTTP_200_OK)
    fcm_servive = FCMNotification(
        api_key="AAAA0lFXPkM:APA91bFp1D6Ghp0n59_T5uRzbJQsmv8IaomrWKrbNuaAWVKUYtbULiiAY-NFMHKMZvdPf71AqRECufbypGz86RaTAhz4fbm_OnG31Rfq2ZYAhiH0rkM_D_Dyuue2dUR729Hh1E7hgBtS")
    message_title = "Booking Confirmed"
    message_body = "Make a visit according to your appointed time",
    # data_message = {
    #     'screen': 'payment'
    # }
    click_action = "FLUTTER_NOTIFICATION_CLICK"
    device_key = device_token
    test = fcm_servive.notify_single_device(registration_id=device_key,
                                            message_body=message_body, message_title=message_title,

                                            )
    print(test)
    return Response(test, status=status.HTTP_200_OK)


# if (message["data"]["screen"]=='payment')
