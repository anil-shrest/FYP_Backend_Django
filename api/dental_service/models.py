from django.db import models
from doctors.models import Doctor


# Dental home services model
class Services(models.Model):
    service_title = models.TextField(max_length=150)
    service_detail = models.TextField(max_length=500)
    service_image = models.ImageField('service_image', blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, related_name='doctor')

    class Meta:
        ordering = ['service_title']

    def __str__(self):
        return self.service_title
