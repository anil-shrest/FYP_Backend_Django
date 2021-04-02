from django.db import models

# Dental home doctor model


class Doctor(models.Model):
    full_name = models.CharField(max_length=150, blank=False)
    nmc_number = models.CharField(max_length=8, blank=False)
    doc_type = models.CharField(max_length=50, blank=False)
    speciality = models.CharField(max_length=200, blank=False)
    photo = models.ImageField('doctors_image', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.full_name
