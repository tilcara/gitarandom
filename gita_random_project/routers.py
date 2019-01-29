from rest_framework import routers
from gitarandom.viewsets import ChapterViewSet, VerseViewSet

router = routers.DefaultRouter()

router.register(r'chapter', ChapterViewSet)
router.register(r'verse', VerseViewSet)