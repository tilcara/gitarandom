from rest_framework import serializers
from .models import Chapter, Verse

class ChapterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Chapter
		fields = '__all__'

class VerseSerializer(serializers.ModelSerializer):
	class Meta:
		model = Verse
		fields = '__all__'
