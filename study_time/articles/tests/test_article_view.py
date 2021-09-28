import pytest

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.permissions import IsAuthenticated

from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.tests import values
from articles.views import ArticleViewSet
from tests.utils import get_client


def test_article_view_serialzier_class():
    assert ArticleViewSet.serializer_class == ArticleSerializer


def test_article_view_permission_classes():
    assert ArticleViewSet.permission_classes == [IsAuthenticated]


@pytest.mark.django_db
def test_article_detail(user_fixture, article_fixture):

    # GIVEN
    article = Article.objects.get()
    client = get_client(user_fixture)

    # WHEN
    request = client.get(values.ARTICLE_DETAIL_PATH)

    # THEN
    assert request.status_code == status.HTTP_200_OK
    assert request.data == {"id": article.id, "title": article.title, "content": article.content}


@pytest.mark.django_db
def test_unauthenticated_user_cannot_access_articles_view(user_fixture):

    # GIVEN
    client = APIClient(user_fixture)

    # WHEN
    request = client.get(values.ARTICLES_LIST_PATH)

    # THEN
    assert request.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_create_article(user_fixture):

    # GIVEN
    client = get_client(user_fixture)
    data = values.DATA_NEW_ARTICLE

    # WHEN
    response = client.post(path=values.ARTICLES_LIST_PATH, data=data, format="json")

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == values.NEW_ARTICLE_RESPONSE


@pytest.mark.django_db
def test_list_articles(user_fixture, three_articles_fixture):

    # GIVEN
    client = get_client(user_fixture)

    # WHEN
    response = client.get(values.ARTICLES_LIST_PATH)

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.ARTICLES_RESPONSE


@pytest.mark.django_db
def test_update_articles(user_fixture, article_fixture):

    # GIVEN
    client = get_client(user_fixture)
    new_data = values.DATA_CHANGED_ARTICLE

    # WHEN
    response = client.put(
        path=values.ARTICLE_DETAIL_PATH, 
        data=new_data, 
        format="json"
        )

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.ARTICLE_UPDATE_RESPONSE


@pytest.mark.django_db
def test_delete_articles(user_fixture, article_fixture):

    # GIVEN
    client = get_client(user_fixture)

    # WHEN
    response = client.delete(path=values.ARTICLE_DETAIL_PATH)

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Article.objects.all().count() == 0
