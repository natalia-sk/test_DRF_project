import pytest

from .factories import ArticleFactory
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
