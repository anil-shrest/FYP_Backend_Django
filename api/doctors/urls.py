from django.urls import path, include
from django.conf.urls import url
from doctors import views

doctor_list = views.DoctorView.as_view({'get': 'list'})

# URLS for doctors
urlpatterns = [
    path('doctor/list/', doctor_list, name='doctor-list'),
    path('doctor/add/',
         views.doctor_view, name='doctor-add'),
]
