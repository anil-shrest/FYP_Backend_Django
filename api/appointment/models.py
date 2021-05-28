from django.db import models
from django.conf import settings
from doctors.models import Doctor
from django.dispatch import receiver


# Class to add appointment
class AppointmentTable(models.Model):

    appointmentBy = models.ForeignKey(Doctor, related_name='doctor_name',
                                      on_delete=models.CASCADE, null=True)
    appointmentTime = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_booked = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='appointments', related_query_name='appointment', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.appointmentTime
