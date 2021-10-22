from rest_framework_extensions.routers import ExtendedSimpleRouter

from .views import CourseViewSet, EpisodeViewSet


router = ExtendedSimpleRouter()
(
    router.register("courses", CourseViewSet, basename="course",).register(
        "episodes",
        EpisodeViewSet,
        basename="episode",
        parents_query_lookups=["course_id"],
    )
)

urlpatterns = router.get_urls()
