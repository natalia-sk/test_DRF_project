import pytest

from articles.tests import values
from .factories import ArticleFactory


@pytest.fixture
def article_fixture():
    return ArticleFactory(id=values.ARTICLE_ID)


@pytest.fixture
def three_articles_fixture():
    text_fields = {
        "title": values.ARTICLE_TITLE, 
        "content": values.ARTICLE_CONTENT
        }
    articles = [ArticleFactory(id=id, **text_fields) for id in values.ARTICLES_IDS]
    return articles
