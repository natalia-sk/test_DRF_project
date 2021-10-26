import pytest

from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from courses.models import Episode
from courses.tests import values
from courses.views import EpisodeViewSet

from tests.utils import get_client


@pytest.mark.django_db
def test_episode_detail(user_fixture, episode_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    request = client.get(values.EPISODE_DETAIL_PATH)

    # THEN
    expected_data = {
        "url": f"http://testserver/courses/episodes/{values.EPISODE_ID}",
        "id": values.EPISODE_ID,
        "title": values.EPISODE_TITLE,
        "video_url": values.EPISODE_VIDEO_URL,
        "course": values.COURSE_ID,
    }

    assert request.status_code == status.HTTP_200_OK
    assert request.data == expected_data


@pytest.mark.parametrize(
    argnames=["action", "expected_permission"],
    argvalues=[
        pytest.param("list",[IsAuthenticated], id="list"),
        pytest.param("create",[IsAuthenticated], id="create"),
        pytest.param("retrieve",[IsAuthenticated], id="retrieve"),
        pytest.param("update",[IsAuthenticated], id="update"),
        pytest.param("partial_update",[IsAuthenticated], id="partial-update"),
        pytest.param("destroy",[IsAuthenticated], id="destroy"),
    ],
)
def test_episode_view_permission_classes(action, expected_permission):
    # GIVEN
    episode_viewset = EpisodeViewSet()
    episode_viewset.action = action
    permissions = [type(permission) for permission in episode_viewset.get_permissions()]

    # THEN
    assert permissions == expected_permission


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["url", "http_method", "expected_status_code"],
    argvalues=[
        pytest.param(values.EPISODES_LIST_PATH, "get", status.HTTP_403_FORBIDDEN, id="list"),
        pytest.param(values.EPISODE_DETAIL_PATH, "get", status.HTTP_403_FORBIDDEN, id="detail-view"),
        pytest.param(values.EPISODES_LIST_PATH, "post", status.HTTP_403_FORBIDDEN, id="create"),
        pytest.param(values.EPISODE_DETAIL_PATH, "put", status.HTTP_403_FORBIDDEN, id="update"),
        pytest.param(values.EPISODE_DETAIL_PATH, "patch", status.HTTP_403_FORBIDDEN, id="partial-update"),
        pytest.param(values.EPISODE_DETAIL_PATH, "delete", status.HTTP_403_FORBIDDEN, id="delete"),
    ],
)
def test_episode_unauthenticated_user_accesses(url, http_method, expected_status_code):
    # GIVEN
    client = get_client()  # unauthenticated user

    # WHEN
    request_function = getattr(client, http_method)
    response = request_function(url)

    # THEN
    assert response.status_code == expected_status_code


@pytest.mark.django_db(reset_sequences=True)
def test_create_episode(user_fixture, course_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user
    data = values.DATA_NEW_EPISODE

    # WHEN
    response = client.post(path=values.EPISODES_LIST_PATH, data=data, format="json")

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == values.NEW_EPISODE_RESPONSE


@pytest.mark.django_db(reset_sequences=True)
def test_list_episodes(user_fixture, three_episodes_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    response = client.get(values.EPISODES_LIST_PATH)

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.EPISODES_RESPONSE


@pytest.mark.django_db
def test_update_episode(user_fixture, episode_fixture, three_courses_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user
    new_data = values.DATA_CHANGED_EPISODE

    # WHEN
    response = client.put(path=values.EPISODE_DETAIL_PATH, data=new_data, format="json")

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.EPISODE_UPDATE_RESPONSE


@pytest.mark.django_db
def test_delete_episode(user_fixture, episode_fixture):
    # GIVEN
    client = get_client(user_fixture)  # authenticated user

    # WHEN
    response = client.delete(path=values.EPISODE_DETAIL_PATH)

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Episode.objects.all().count() == 0
