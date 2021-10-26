import pytest

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from articles.models import Article
from articles.tests import values
from articles.views import ArticleViewSet

from tests.utils import get_client


@pytest.mark.django_db
def test_article_detail(user_fixture, article_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    request = client.get(values.ARTICLE_DETAIL_PATH)

    # THEN
    expected_data = {
        "id": values.ARTICLE_ID,
        "title": values.ARTICLE_TITLE,
        "content": values.ARTICLE_CONTENT,
    }

    assert request.status_code == status.HTTP_200_OK
    assert request.data == expected_data


@pytest.mark.parametrize(
    argnames=["action", "expected_permission"],
    argvalues=[
        pytest.param("list", [IsAuthenticated], id="list"),
        pytest.param("create", [IsAuthenticated], id="create"),
        pytest.param("retrieve", [IsAuthenticated], id="retrieve"),
        pytest.param("update", [IsAuthenticated], id="update"),
        pytest.param("partial_update", [IsAuthenticated], id="partial-update"),
        pytest.param("destroy", [IsAuthenticated], id="destroy"),
    ],
)
def test_course_view_permission_classes(action, expected_permission):
    # GIVEN
    article_viewset = ArticleViewSet()
    article_viewset.action = action
    permissions = [type(permission) for permission in article_viewset.get_permissions()]

    # THEN
    assert permissions == expected_permission


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["url", "http_method", "expected_status_code"],
    argvalues=[
        pytest.param(values.ARTICLES_LIST_PATH, "get", status.HTTP_403_FORBIDDEN, id="list"),
        pytest.param(values.ARTICLE_DETAIL_PATH, "get", status.HTTP_403_FORBIDDEN, id="detail-view"),
        pytest.param(values.ARTICLES_LIST_PATH, "post", status.HTTP_403_FORBIDDEN, id="create"),
        pytest.param(values.ARTICLE_DETAIL_PATH, "put", status.HTTP_403_FORBIDDEN, id="update"),
        pytest.param(values.ARTICLE_DETAIL_PATH, "patch", status.HTTP_403_FORBIDDEN, id="partial-update"),
        pytest.param(values.ARTICLE_DETAIL_PATH, "delete", status.HTTP_403_FORBIDDEN, id="delete"),
    ],
)
def test_article_unauthenticated_user_accesses(url, http_method, expected_status_code):
    # GIVEN
    client = get_client()  # unauthenticated user

    # WHEN
    request_function = getattr(client, http_method)
    response = request_function(url)

    # THEN
    assert response.status_code == expected_status_code


@pytest.mark.django_db
def test_create_article(user_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user
    data = values.DATA_NEW_ARTICLE

    # WHEN
    response = client.post(path=values.ARTICLES_LIST_PATH, data=data, format="json")

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == values.NEW_ARTICLE_RESPONSE


@pytest.mark.django_db
def test_list_articles(user_fixture, three_articles_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    response = client.get(values.ARTICLES_LIST_PATH)

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.ARTICLES_RESPONSE


@pytest.mark.django_db
def test_update_articles(user_fixture, article_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user
    new_data = values.DATA_CHANGED_ARTICLE

    # WHEN
    response = client.put(path=values.ARTICLE_DETAIL_PATH, data=new_data, format="json")

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.ARTICLE_UPDATE_RESPONSE


@pytest.mark.django_db
def test_delete_articles(user_fixture, article_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    response = client.delete(path=values.ARTICLE_DETAIL_PATH)

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Article.objects.all().count() == 0
