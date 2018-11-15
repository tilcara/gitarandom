from django.db import models

# Create your models here.

class Chapter(models.Model):
	chapter_number = models.IntegerField()
	chapter_summary = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	name_meaning = models.CharField(max_length=100)
	name_translation = models.CharField(max_length=100)
	name_transliterated = models.CharField(max_length=100)
	verses_count = models.IntegerField()

class Verse(models.Model):
	chapter_number = models.IntegerField()
	meaning = models.CharField(max_length=1000)
	text = models.CharField(max_length=300)
	transliteration = models.CharField(max_length=300)
	verse_number = models.CharField(max_length=100)
	word_meanings = models.CharField(max_length=300)