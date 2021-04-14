from django.urls import path, include
from django.conf.urls import url
from device_token import views


# URLS for device token set
urlpatterns = [
    # path('device_token/list/', service_list, name='service-list'),
    #     path('service/edit/<int:pk>/', service_edit, name='service-edit'),
    #     path('service/edit/<int:pk>/', views.service_update, name='service-edit'),
    # path('device_token/add/', views.get_device_token, name='device-add'),
    path('save_device_token/', views.save_device_key, name="device_key_val"),
    path('update_device_token/<int:author_id>/', views.update_device_key,
         name="device_key_val_update"),

]
