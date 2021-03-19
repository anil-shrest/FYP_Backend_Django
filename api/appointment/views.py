from django.shortcuts import render
from .models import AppointmentTable
from .serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status, generics, request, viewsets
from account.models import NewUser
from .serializers import UserSerializer
# from django.http import request
User = NewUser

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# # Appointment classes for CRUD


class AppointmentView(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = AppointmentTable.objects.all()
    serializer_class = AppointmentSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.NewUser)


class AppointmentList(generics.ListCreateAPIView):
    # List all appointments, or create a new one.
    permission_classes = (permissions.IsAuthenticated,)
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
    #     serializer.save(owner=self.request.NewUser)


class AppointmentEdit(generics.RetrieveUpdateDestroyAPIView):
    # Retrieve, update or delete a appointment instance.
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = AppointmentTable.objects.all()
    serializer_class = AppointmentSerializer


# Using viewsets
# class ViewAllAppoints(viewsets.ModelViewSet):
#     serializer_class = AppointmentSerializer
#     queryset = AppointmentTable.objects.all()
