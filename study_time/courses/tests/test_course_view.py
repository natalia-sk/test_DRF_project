import pytest

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from courses.models import Course
from courses.tests import values
from courses.views import CourseViewSet

from tests.utils import get_client


@pytest.mark.django_db
def test_course_detail(user_fixture, course_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    request = client.get(values.COURSE_DETAIL_PATH)

    # THEN
    expected_data = {
        "id": values.COURSE_ID,
        "title": values.COURSE_TITLE,
        "video_duration": values.COURSE_VIDEO_DURATION,
        "language": values.COURSE_LANGUAGE,
        "episodes": [],
    }

    assert request.status_code == status.HTTP_200_OK
    assert request.data == expected_data


@pytest.mark.parametrize(
    argnames=["action"],
    argvalues=[
        pytest.param("list", id="list"),
        pytest.param("create", id="create"),
        pytest.param("retrieve", id="retrieve"),
        pytest.param("update", id="update"),
        pytest.param("partial_update", id="partial-update"),
        pytest.param("destroy", id="destroy"),
    ],
)
def test_course_view_permission_classes(action):
    # GIVEN
    course_viewset = CourseViewSet()
    course_viewset.action = action
    permissions = [type(permission) for permission in course_viewset.get_permissions()]

    # THEN
    assert permissions == [IsAuthenticated]


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["url", "http_method"],
    argvalues=[
        pytest.param(values.COURSES_LIST_PATH, "get", id="list"),
        pytest.param(values.COURSE_DETAIL_PATH, "get", id="detail-view"),
        pytest.param(values.COURSES_LIST_PATH, "post", id="create"),
        pytest.param(values.COURSE_DETAIL_PATH, "put", id="update"),
        pytest.param(values.COURSE_DETAIL_PATH, "patch", id="partial-update"),
        pytest.param(values.COURSE_DETAIL_PATH, "delete", id="delete"),
    ],
)
def test_course_endpoints_forbidden_for_anonymous(url, http_method):
    # GIVEN
    client = get_client()  # unauthenticated user

    # WHEN
    request_function = getattr(client, http_method)
    response = request_function(url)

    # THEN
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db(reset_sequences=True)
def test_create_course(user_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user
    data = values.DATA_NEW_COURSE

    # WHEN
    response = client.post(path=values.COURSES_LIST_PATH, data=data, format="json")

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == values.NEW_COURSE_RESPONSE


@pytest.mark.django_db
def test_list_curses(user_fixture, three_courses_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    response = client.get(values.COURSES_LIST_PATH)

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.COURSES_RESPONSE


@pytest.mark.django_db
def test_update_course(user_fixture, course_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user
    new_data = values.DATA_CHANGED_COURSE

    # WHEN
    response = client.put(path=values.COURSE_DETAIL_PATH, data=new_data, format="json")

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.COURSE_UPDATE_RESPONSE


@pytest.mark.django_db
def test_delete_course(user_fixture, course_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    response = client.delete(path=values.COURSE_DETAIL_PATH)

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Course.objects.all().count() == 0
