from rest_framework import viewsets
from .models import Chapter, Verse
from .serializers import ChapterSerializer, VerseSerializer

class ChapterViewSet(viewsets.ModelViewSet):
	queryset = Chapter.objects.all()
	serializer_class = ChapterSerializer

class VerseViewSet(viewsets.ModelViewSet):
	queryset = Verse.objects.all()
	serializer_class = VerseSerializer