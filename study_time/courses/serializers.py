from rest_framework import serializers
from .models import Course, Episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ["id", "title", "video_url", "course"]


class CourseSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "video_duration", "language", "episodes"]
