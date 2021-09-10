import pytest

from .factories import ArticleFactory
from articles.serializers import ArticleSerializer
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


def test_serializer_contains_expected_fields():
    # GIVEN
    serializer = ArticleSerializer()
    # WHEN
    serializer_fields = serializer.fields
    # THEN
    assert set(serializer_fields.keys()) == set(['id', 'title', 'content'])
