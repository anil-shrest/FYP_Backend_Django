from rest_framework import serializers
from .models import NotesTable
from account.models import NewUser


# Adding Notes Serializer
class NotesSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_author_username')

    class Meta:
        model = NotesTable
        fields = [
            'id', 'note_title', 'note_description', 'username'
        ]

    def get_author_username(self, notes):
        username = notes.author.username
        return username


class UserSerializer(serializers.ModelSerializer):
    appointment = serializers.PrimaryKeyRelatedField(
        many=True, queryset=NotesTable.objects.all())

    class Meta:
        model = NewUser
        fields = ['id', 'username', 'notes']
