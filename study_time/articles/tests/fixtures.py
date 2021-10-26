import pytest

from articles.tests import values
from .factories import ArticleFactory


@pytest.fixture
def article_fixture():
    return ArticleFactory(
        id=values.ARTICLE_ID,
        title=values.ARTICLE_TITLE,
        content=values.ARTICLE_CONTENT,
    )


@pytest.fixture
def three_articles_fixture(article_fixture):
    articles = [article_fixture]
    text_fields = {
        "title": values.ARTICLE_TITLE, 
        "content": values.ARTICLE_CONTENT,
    }
    articles += [ArticleFactory(id=id, **text_fields) for id in values.ARTICLES_IDS[1:3]]
    return articles
