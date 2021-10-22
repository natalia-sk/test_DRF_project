from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import CourseViewSet, EpisodeViewSet

from .apps import CoursesConfig

# router = DefaultRouter(trailing_slash=False)

# router2 = DefaultRouter(trailing_slash=False)

# router.register(r"courses", CourseViewSet, "course")
# router2.register(r"episodes", EpisodeViewSet, "episode")

# urlpatterns = [
#     path("", include(router.urls)),
#     path("courses/<course_id>/", include(router2.urls))  #get_urls
# ]

app_name = CoursesConfig.name

router = ExtendedSimpleRouter()
(
    router.register("courses", CourseViewSet, basename="course",)
    .register(
        "episodes",
        EpisodeViewSet,
        basename="episode",
        parents_query_lookups=["course_id"],
    )
)

urlpatterns = router.get_urls()
