from django.db import models
from account.models import NewUser


# Device key storage model

class DeviceToken(models.Model):
    device_key = models.TextField(max_length=350)
    author = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, null=True, related_name='staffUser')

    class Meta:
        ordering = ['author']

    def __str__(self):
        return self.device_key
