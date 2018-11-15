
from django.shortcuts import render
import json
import random
from .models import Verse, Chapter



def home(request):
	return render(request,'gitarandom/index.html')

def random_verse(request):
	random.seed()
	chapter_number = random.randint(1, 18)
	chapter = Chapter.objects.get(chapter_number=chapter_number)
	verses_amount = chapter.verses_count
	verse_number = random.randint(1, verses_amount)
	verse = Verse.objects.filter(chapter_number=chapter_number).get(verse_number=verse_number)
	context = {'verse': verse}
	return render(request,'gitarandom/random_verse.html',context)



