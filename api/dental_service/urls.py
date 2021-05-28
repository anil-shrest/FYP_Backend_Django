from django.urls import path, include
from django.conf.urls import url
from dental_service import views


service_list = views.ServiceView.as_view({'get': 'list'})

# URLS for service task
urlpatterns = [
    path('service/list/', service_list, name='service-list'),
    #     path('service/edit/<int:pk>/', service_edit, name='service-edit'),
    #     path('service/edit/<int:pk>/', views.service_update, name='service-edit'),
    path('service/add/', views.service_view, name='service-add'),
    path('services/',
         views.DoctorServiceView.as_view({'get': 'list'})),
]
