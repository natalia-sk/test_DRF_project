import pytest

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.permissions import IsAuthenticated

from .factories import ArticleFactory
from articles.models import Article
from articles.serializers import ArticleSerializer
from articles.views import ArticleViewSet
from tests.utils import get_client


def test_article_view_serialzier_class():
    assert ArticleViewSet.serializer_class == ArticleSerializer


def test_article_view_permission_classes():
    assert ArticleViewSet.permission_classes == [IsAuthenticated]


@pytest.mark.django_db
def test_authenticated_user_can_access_article_details(user_fixture):

    # GIVEN
    article = ArticleFactory()
    client = get_client(user_fixture)

    # WHEN
    request = client.get(reverse("articles-detail", kwargs={"pk": article.pk}))

    # THEN
    assert request.status_code == status.HTTP_200_OK
    assert request.data == {"id": article.id, "title": article.title, "content": article.content}


@pytest.mark.django_db
def test_unauthenticated_user_cannot_access_articles_view(user_fixture):

    # GIVEN
    client = APIClient(user_fixture)

    # WHEN
    request = client.get(reverse("articles-list"))

    # THEN
    assert request.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_create_article(user_fixture):

    # GIVEN
    client = get_client(user_fixture)
    data = {
        "title": "test article title",
        "content": "test article content"
    }

    # WHEN
    response = client.post(path=reverse("articles-list"), data=data, format="json")

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
    assert Article.objects.get().id == response.json()["id"]
    assert Article.objects.get().title == response.json()["title"]
    assert Article.objects.get().content == response.json()["content"]


@pytest.mark.django_db
def test_list_articles(user_fixture):

    # GIVEN
    client = get_client(user_fixture)
    ArticleFactory.create_batch(3)

    # WHEN
    response = client.get(reverse("articles-list"))

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()["results"]) == 3


@pytest.mark.django_db
def test_update_articles(user_fixture):

    # GIVEN
    client = get_client(user_fixture)
    article = ArticleFactory()
    new_data = {
        "title": "test new article title",
        "content": "test new article content"
    }

    # WHEN
    response = client.put(
        path=reverse("articles-detail", kwargs={"pk": article.id}), 
        data=new_data, 
        format="json"
        )

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert Article.objects.get().id == response.json()["id"]
    assert Article.objects.get().title == response.json()["title"]
    assert Article.objects.get().content == response.json()["content"]


@pytest.mark.django_db
def test_delete_articles(user_fixture):

    # GIVEN
    client = get_client(user_fixture)
    article = ArticleFactory()

    # WHEN
    response = client.delete(path=reverse("articles-detail", kwargs={"pk": article.id}))

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Article.objects.all().count() == 0
