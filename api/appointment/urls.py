from django.urls import path, include
from django.conf.urls import url
from appointment import views


# URLS for appointment task
urlpatterns = [
    path('appointment/list/', views.AppointmentList.as_view(),
         name='appointment-list'),
    path('appointment/edit/<int:pk>',
         views.AppointmentEdit.as_view(), name='appointment-edit'),
]
