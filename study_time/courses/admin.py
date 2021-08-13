from django.contrib import admin
from .models import Course, Episode


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    pass
