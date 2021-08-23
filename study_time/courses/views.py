from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Course, Episode
from .serializers import CourseSerializer, EpisodeSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['title']


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['language']
    ordering_fields = ['title']
