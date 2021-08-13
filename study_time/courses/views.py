from rest_framework import viewsets

from .models import Course, Episode
from .serializers import CourseSerializer, EpisodeSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer

    def get_queryset(self):
        return Episode.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.all()
