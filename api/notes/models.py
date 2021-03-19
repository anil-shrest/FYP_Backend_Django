from django.db import models
from django.conf import settings


# Model class to add notes
class NotesTable(models.Model):
    note_title = models.TextField(max_length=150)
    note_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='notes', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.note_title
