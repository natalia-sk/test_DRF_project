import pytest

from rest_framework.test import APIClient
from rest_framework.permissions import IsAuthenticated

from .factories import ArticleFactory
from articles.serializers import ArticleSerializer
from articles.views import ArticleViewSet
from tests.utils import get_client


@pytest.mark.django_db
def test_authenticated_user_can_access_article_details(user_fixture):
    # GIVEN
    article = ArticleFactory()
    client = get_client(user_fixture)
    # WHEN
    request = client.get('/articles/articles/1')
    # THEN
    assert request.status_code == 200
    assert request.data == {"id": article.id, "title": article.title, "content": article.content}


@pytest.mark.django_db
def test_unauthenticated_user_cannot_access_articles_view(user_fixture):
    # GIVEN
    client = APIClient(user_fixture)
    # WHEN
    request = client.get('/articles/articles')
    # THEN
    assert request.status_code == 403


def test_article_view_serialzier_class():
    assert ArticleViewSet.serializer_class == ArticleSerializer


def test_article_view_permission_classes():
    assert ArticleViewSet.permission_classes == [IsAuthenticated]
