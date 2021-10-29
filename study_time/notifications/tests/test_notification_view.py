import pytest

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from notifications.models import Notification
from notifications.tests import values
from notifications.views import NotificationViewSet
from tests.utils import get_client

from articles.models import Article
from articles.tests import values as article_values
from courses.tests import values as course_values


@pytest.mark.django_db(reset_sequences=True)
def test_notification_detail(user_fixture, course_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    response = client.get(values.NOTIFICATION_DETAIL_PATH)

    # THEN
    expected_data = {
        "id": values.NOTIFICATION_ID,
        "title": f"New course: {course_values.COURSE_TITLE}",
        "body": f"Hey, there's a new course: {course_values.COURSE_TITLE} ({course_values.COURSE_VIDEO_DURATION}s)",
        "content_type": "Course",
        "article": None,
        "course": course_values.COURSE_ID,
        "episode": None,
    }

    assert response.status_code == status.HTTP_200_OK
    assert response.data == expected_data


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
def test_notification_view_permission_classes(action, expected_permission):
    # GIVEN
    notification_viewset = NotificationViewSet()
    notification_viewset.action = action
    permissions = [
        type(permission) for permission in notification_viewset.get_permissions()
    ]

    # THEN
    assert permissions == expected_permission


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["url", "http_method", "expected_status_code"],
    argvalues=[
        pytest.param(
            values.NOTIFICATIONS_LIST_PATH,
            "get",
            status.HTTP_403_FORBIDDEN,
            id="list",
        ),
        pytest.param(
            values.NOTIFICATION_DETAIL_PATH,
            "get",
            status.HTTP_403_FORBIDDEN,
            id="detail-view",
        ),
        pytest.param(
            values.NOTIFICATIONS_LIST_PATH,
            "post",
            status.HTTP_403_FORBIDDEN,
            id="create",
        ),
        pytest.param(
            values.NOTIFICATION_DETAIL_PATH,
            "put",
            status.HTTP_403_FORBIDDEN,
            id="update",
        ),
        pytest.param(
            values.NOTIFICATION_DETAIL_PATH,
            "patch",
            status.HTTP_403_FORBIDDEN,
            id="partial-update",
        ),
        pytest.param(
            values.NOTIFICATION_DETAIL_PATH,
            "delete",
            status.HTTP_403_FORBIDDEN,
            id="delete",
        ),
    ],
)
def test_notification_unauthenticated_user_accesses(
    url, http_method, expected_status_code
):
    # GIVEN
    client = get_client()  # unauthenticated user

    # WHEN
    request_function = getattr(client, http_method)
    response = request_function(url)

    # THEN
    assert response.status_code == expected_status_code


@pytest.mark.django_db(reset_sequences=True)
def test_list_notifications(user_fixture, three_courses_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    response = client.get(values.NOTIFICATIONS_LIST_PATH)

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.NOTIFICATIONS_RESPONSE


@pytest.mark.django_db(reset_sequences=True)
def test_notification_delete(user_fixture, course_fixture):
    # GIVEN
    client = get_client(user_fixture)

    # WHEN
    response = client.delete(path=values.NOTIFICATION_DETAIL_PATH)

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Notification.objects.all().count() == 0


@pytest.mark.django_db(reset_sequences=True)
def test_notification_deleted_after_article_is_deleted(user_fixture, article_fixture):
    # GIVEN
    client = get_client(user_fixture)

    # WHEN
    assert Notification.objects.all().count() == 1  # ? in "WHEN" ?
    response = client.delete(path=article_values.ARTICLE_DETAIL_PATH)

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Notification.objects.all().count() == 0
    assert Article.objects.all().count() == 0

