from django.db import models
from django.conf import settings
from doctors.models import Doctor
from django.dispatch import receiver


# Model creation for tiime table
class TimeTable(models.Model):

    time_space = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.OneToOneField(Doctor, related_name='doctors',
                                  on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.time_space
