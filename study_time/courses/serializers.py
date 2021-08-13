from rest_framework import serializers
from .models import Course, Episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ["url", "id", "title", "video_url", "course"]


class CourseSerializer(serializers.ModelSerializer):
    episode_set = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["url", "id", "title", "video_duration", "language", "episode_set"]
