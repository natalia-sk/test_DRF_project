from django.urls import path, include
# from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"articles", ArticleViewSet, "articles")

urlpatterns = [
    path("", include(router.urls)),
]
