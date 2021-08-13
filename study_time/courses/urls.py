from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, EpisodeViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"courses", CourseViewSet, "course")
router.register(r"episodes", EpisodeViewSet, "episode")

urlpatterns = [
    path("", include(router.urls)),
]
