from rest_framework import serializers
from .models import Course, Episode


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = ["id", "title", "video_url"]

    def create(self, validated_data):
        validated_data["course_id"] = self._get_course_id()
        return super().create(validated_data)

    def _get_course_id(self) -> int:
        view = self.context["view"]
        course_id = view.kwargs[view.course_id_lookup]
        return course_id


class CourseSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ["id", "title", "video_duration", "language", "episodes"]
