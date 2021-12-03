from rest_framework import viewsets
from rest_framework_extensions.mixins import NestedViewSetMixin
from django_filters.rest_framework import DjangoFilterBackend

from .models import Course, Episode
from .serializers import CourseSerializer, EpisodeSerializer


class EpisodeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer
    queryset = Episode.objects.all()
    course_id_lookup = "parent_lookup_course_id"


class CourseViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["language"]
