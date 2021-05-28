from django.urls import path, include
from django.conf.urls import url
from device_token import views


# URLS for device token set
urlpatterns = [
    path('save_device_token/', views.save_device_key, name="device_key_val"),
    path('update_device_token/', views.update_device_key,
         name="device_key_val_update"),
]
