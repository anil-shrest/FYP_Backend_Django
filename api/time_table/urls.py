from django.urls import path, include
from django.conf.urls import url
from time_table import views


# URLS for appointment task
urlpatterns = [
    path('time_table/list/', views.TimeTableView.as_view({'get': 'list'}),
         name='time_table-list'),
    path('time_table/details/<int:id>/', views.TimeTableDetailView.as_view(),
         name='time_table-details'),
    path('time_table/add/<int:id>/',
         views.set_timings, name='add-timings'),
    path('time_table/edit/<int:pk>',
         views.TimeTableEdit.as_view(), name='time_table-edit'),
]
