from django.db import models


class Notification(models.Model):
    class ContentTypeChoices(models.TextChoices):
        ARTICLE = "Article"
        COURSE = "Course"
        EPISODE = "Episode"

    title = models.CharField(max_length=120)
    body = models.TextField()
    content_type = models.CharField(
        choices=ContentTypeChoices.choices,
        max_length=10)
