from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Notification
from articles.models import Article
from courses.models import Course, Episode

@receiver(post_save, sender=Course) 
def create_course_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title = f"New course: {instance.title}",
            body = f"Hey, there's a new course: {instance.title} ({instance.video_duration}s)",
            content_type = "Course",
            course=instance)

@receiver(post_save, sender=Episode) 
def create_episode_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title = f"New episode: {instance.title}",
            body = f"Hey, there's a new episode: {instance.title} (in {instance.course.title} course)",
            content_type = "Episode",
            episode=instance)

@receiver(post_save, sender=Article) 
def create_article_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title = f"New article: {instance.title}",
            body = f"Hey, there's a new article: {instance.title}",
            content_type = "Article",
            article=instance)
