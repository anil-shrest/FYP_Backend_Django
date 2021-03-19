from django.urls import path, include
from django.conf.urls import url
from notes import views

urlpatterns = [
    path('notes/list/', views.NotesList.as_view(),
         name='notes_list'),
         path('notes/edit/<int:pk>', views.NotesEdit.as_view(), name='notes_edit'),
]
