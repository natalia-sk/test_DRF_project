from django.db import models


class Notification(models.Model):
    class ContentTypeChoices(models.TextChoices):
        ARTICLE = "Article"
        COURSE = "Course"
        EPISODE = "Episode"

    title = models.CharField(max_length=120)
    body = models.TextField()
    content_type = models.CharField(choices=ContentTypeChoices.choices, max_length=10)
    article = models.ForeignKey("articles.Article", on_delete=models.CASCADE, null=True)
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE, null=True)
    episode = models.ForeignKey("courses.Episode", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["id"]
