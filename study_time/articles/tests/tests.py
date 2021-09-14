import pytest
import re
from django.db.utils import DataError
from rest_framework.test import APIClient
from rest_framework.permissions import IsAuthenticated

from .factories import ArticleFactory
from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.views import ArticleViewSet
from tests.utils import get_client


@pytest.mark.django_db
def test_article(user_fixture):
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


def test_serializer_contains_expected_fields():
    # GIVEN
    serializer = ArticleSerializer()
    # WHEN
    serializer_fields = serializer.fields
    # THEN
    assert set(serializer_fields.keys()) == set(['id', 'title', 'content'])


@pytest.mark.django_db
def test_article_model_raises_exception():
    # THEN
    with pytest.raises(DataError, match=re.escape("value too long for type character varying(150)")):
        # WHEN
        Article.objects.create(title=f"{'test' * 150}", content="test content")


def test_article_view_serialzier_class():
    assert ArticleViewSet.serializer_class == ArticleSerializer


def test_article_view_permission_classes():
    assert ArticleViewSet.permission_classes == [IsAuthenticated]
