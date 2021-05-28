from django.db import models
# from amodels import NewUser
from django.conf import settings



# Device key storage model
class DeviceToken(models.Model):
    device_key = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='staffUser')

    class Meta:
        ordering = ['author']

    def __str__(self):
        return self.device_key
