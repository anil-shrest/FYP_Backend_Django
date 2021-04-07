from django.urls import path, include
from django.conf.urls import url
from appointment import views


# URLS for appointment task
urlpatterns = [
    path('appointment/list/', views.AppointmentView.as_view({'get': 'list'}),
         name='appointment-list'),
    path('appointment/list-details/<int:id>/', views.AppointmentDetailView.as_view(),
         name='appointment-list'),
    path('appointment/edit/<int:pk>/',
         views.AppointmentEdit.as_view(), name='appointment-edit'),
    path('appointment/add/<int:id>/', views.book_appointments, name='add-appoint'),
    path('sending_fcm/<int:staff_id>/',
         views.sending_notification, name='add-fcm'),
    path('confirmed_fcm/<int:appointment_id>/',
         views.sending_confirmation_notification, name='confirm-fcm'),
]
