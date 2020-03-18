from django.shortcuts import render
from rest_framework import viewsets
#Rather than write multiple views we're grouping together all the common behavior into classes called ViewSets.
from note.note_api import NoteSerialiser
from note.models import Note
# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the smaple note index.")


class NoteViewSet (viewsets.ModelViewSet):
    queryset=Note.objects.all()
    serializer_class = NoteSerialiser