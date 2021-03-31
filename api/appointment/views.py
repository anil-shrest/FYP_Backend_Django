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
from rest_framework.decorators import api_view, permission_classes
# from django.http import request
User = NewUser

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Appointment classes for CRUD

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


class AppointmentView(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = AppointmentTable.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.NewUser)


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
