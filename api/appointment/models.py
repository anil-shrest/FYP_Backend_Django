from django.db import models
from django.conf import settings
from doctors.models import Doctor
# from django.utils.text import slugify
from django.dispatch import receiver
# from django.db.models.signals import post_delete, pre_save


# Class to add appointment

class AppointmentTable(models.Model):

    # appointmentBy = models.TextField(max_length=50)
    appointmentBy = models.ForeignKey(Doctor, related_name='doctor_name',
                                      on_delete=models.CASCADE, null=True)
    appointmentTime = models.TextField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='appointments', related_query_name='appointment', on_delete=models.CASCADE, null=True)
    # slug = models.SlugField(blank=True, unique=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.appointmentTime


# @receiver(post_delete, sender=AppointmentTable)
# def submission_delete(sender, instance, **kwargs):
# 	instance.image.delete(False)

# def pre_save_appointment_receiever(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = slugify(instance.owner.username + "-" + instance.id)

# pre_save.connect(pre_save_appointment_receiever, sender=AppointmentTable)
