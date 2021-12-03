from django.db import models
from utils.constants import LanguagesChoices


class Course(models.Model):
    title = models.CharField(max_length=150)
    video_duration = models.PositiveIntegerField(help_text="in seconds")
    language = models.CharField(
        max_length=10, choices=LanguagesChoices.choices, default="en"
    )

    class Meta:
        ordering = ["id"]


class Episode(models.Model):
    title = models.CharField(max_length=150)
    video_url = models.URLField(max_length=200)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="episodes"
    )

    class Meta:
        ordering = ["id"]
