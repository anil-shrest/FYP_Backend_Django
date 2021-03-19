from django.urls import path, include
from django.conf.urls import url
from doctors import views

doctor_list = views.DoctorView.as_view({'get': 'list'})

# URLS for doctors
urlpatterns = [
    path('doctor/list/', doctor_list, name='doctor-list'),
    #     path('service/edit/<int:pk>/', service_edit, name='service-edit'),
    #     path('service/edit/<int:pk>/', views.service_update, name='service-edit'),
    path('doctor/add/',
         views.doctor_view, name='doctor-add'),
]
