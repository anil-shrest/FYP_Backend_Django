from django.shortcuts import render
from .models import NotesTable
from .serializers import NotesSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status, generics, request
from account.models import NewUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
User = NewUser


# class NotesList(generics.ListCreateAPIView):
#     # List all appointments, or create a new one.
#     # permission_classes = (permissions.IsAuthenticated,)
#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = [permissions.IsAdminUser]
#     queryset = NotesTable.objects.all()
#     # queryset = AppointmentTable.objects.filter(
#     #             username=request.user)
#     serializer_class = NotesSerializer

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)


# class NotesEdit(generics.RetrieveUpdateDestroyAPIView):
#     # Retrieve, update or delete a appointment instance.
#     # permission_classes = [permissions.IsAuthenticated]

#     queryset = NotesTable.objects.all()
#     serializer_class = NotesSerializer

class NotesList(generics.ListCreateAPIView):
    # List all appointments, or create a new one.
    permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [permissions.IsAdminUser]
    # queryset = NotesTable.objects.all()
    # queryset = AppointmentTable.objects.filter(
    #             username=request.user)
    serializer_class = NotesSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = NotesTable.objects.all()
        if user is not None:
            queryset = queryset.filter(author=user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Using generics
class NotesEdit(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = NotesSerializer
    queryset = NotesTable.objects.all()
    # permission_classes = [IsAccountAdminOrReadOnly]
