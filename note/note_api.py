#like form but for serializing data
from rest_framework import serializers , viewsets
#Serializers are used to convert data from different formats like JSON, XMl to complex data types like querysets
from .models import Note

class NoteSerialiser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Note
        fields = ('id', 'title', 'description', 'created_at', 'created_by', 'priority')

# class NoteViewSet(viewsets.ModelViewSet):
#     queryset = Note.objects.all()
#     serializer_class =NoteSerialiser