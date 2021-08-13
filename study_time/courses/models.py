from django.db import models


class Course(models.Model):
    LANGUAGE_CHOICE = (
        ("en", "English"),
        ("ru", "Russian"),
        ("de", "German"),
        ("fr", "French")
    )

    title = models.CharField(max_length=150)
    video_duration = models.PositiveIntegerField()
    language = models.CharField(
        max_length=10,
        choices=LANGUAGE_CHOICE, default="en")


class Episode(models.Model):
    title = models.CharField(max_length=150)
    video_url = models.URLField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
