import pytest

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIClient

from courses.models import Episode
from courses.serializers import EpisodeSerializer
from courses.tests import values
from courses.views import EpisodeViewSet
from tests.utils import get_client


def test_episode_view_serialzier_class():
    assert EpisodeViewSet.serializer_class == EpisodeSerializer


def test_episode_view_permission_classes():
    assert EpisodeViewSet.permission_classes == [IsAuthenticated]
    

@pytest.mark.django_db
def test_episode_detail(user_fixture, episode_fixture):

    # GIVEN
    episode = Episode.objects.get()
    client = get_client(user_fixture)
    expected_data = {
        "url": f"http://testserver/courses/episodes/{episode.id}", 
        "id": episode.id,
        "title": episode.title,
        "video_url": episode.video_url,
        "course": episode.course.id
    }

    # WHEN
    request = client.get(values.EPISODE_DETAIL_PATH)

    # THEN
    assert request.status_code == status.HTTP_200_OK
    assert request.data == expected_data


@pytest.mark.django_db
def test_unauthenticated_user_cannot_access_episodes_view(user_fixture):

    # GIVEN
    client = APIClient(user_fixture)

    # WHEN
    request = client.get(values.EPISODES_LIST_PATH)

    # THEN
    assert request.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db(reset_sequences=True)
def test_create_episode(user_fixture, course_fixture):
    
    # GIVEN
    client = get_client(user_fixture)
    data = values.DATA_NEW_EPISODE

    # WHEN
    response = client.post(path=values.EPISODES_LIST_PATH, data=data, format="json")

    # THEN
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == values.NEW_EPISODE_RESPONSE


@pytest.mark.django_db(reset_sequences=True)
def test_list_episodes(user_fixture, three_episodes_fixture):
    
    # GIVEN
    client = get_client(user_fixture)

    # WHEN
    response = client.get(values.EPISODES_LIST_PATH)

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.EPISODES_RESPONSE


@pytest.mark.django_db
def test_update_episode(user_fixture, episode_fixture, three_courses_fixture):
    
    # GIVEN
    client = get_client(user_fixture)
    new_data = values.DATA_CHANGED_EPISODE

    # WHEN
    response = client.put(
        path=values.EPISODE_DETAIL_PATH,
        data=new_data,
        format="json"
    )

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.EPISODE_UPDATE_RESPONSE


@pytest.mark.django_db
def test_delete_episode(user_fixture, episode_fixture):
    
    # GIVEN
    client = get_client(user_fixture)

    # WHEN
    response = client.delete(path=values.EPISODE_DETAIL_PATH)

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Episode.objects.all().count() == 0
