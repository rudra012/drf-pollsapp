from rest_framework import routers

from tracks.views import QuestionViewSet, TrackViewSet

router = routers.DefaultRouter()
router.register(r'tracks', TrackViewSet)
router.register(r'questions', QuestionViewSet)
