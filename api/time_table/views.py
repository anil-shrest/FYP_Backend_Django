from django.shortcuts import get_object_or_404, render
from .models import TimeTable
from .serializers import TimeTableSerializer, TimeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status, generics, request, viewsets
from rest_framework.decorators import api_view, permission_classes
from doctors.models import Doctor
from requests.models import Response
from rest_framework.response import Response
from rest_framework.views import APIView


# Time table classes for CRUD

class TimeTableView(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.NewUser)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def set_timings(request, id):
    releated_doctor = Doctor.objects.get(id=id)
    if request.method == 'POST':
        serializer = TimeSe(data=request.data)
        if serializer.is_valid():
            serializer.save(doctor=releated_doctor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class TimeTableEdit(generics.RetrieveUpdateDestroyAPIView):
    # Retrieve, update or delete a appointment instance.
    # permission_classes = [permissions.IsAuthenticated]

    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer


class TimeTableDetailView(APIView):

    def patch(self, request, *args, **kwargs):
        time = get_object_or_404(TimeTable, pk=kwargs['id'])
        serializer = TimeSerializer(
            time, data=request.data, partial=True)
        if serializer.is_valid():
            time = serializer.save()
            return Response(TimeSerializer(time).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        time = get_object_or_404(TimeTable, pk=kwargs['id'])
        time.delete()
        return Response("Time space deleted", status=status.HTTP_204_NO_CONTENT)
