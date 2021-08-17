from rest_framework import viewsets

from .models import Course, Episode
from .serializers import CourseSerializer, EpisodeSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
