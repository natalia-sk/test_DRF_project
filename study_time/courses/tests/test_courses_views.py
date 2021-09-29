import pytest

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.test import APIClient

from courses.models import Course, Episode
from courses.serializers import CourseSerializer, EpisodeSerializer
from courses.tests import values
from courses.views import CourseViewSet, EpisodeViewSet
from tests.utils import get_client


def test_course_view_serialzier_class():
    assert CourseViewSet.serializer_class == CourseSerializer


def test_course_view_permission_classes():
    assert CourseViewSet.permission_classes == [IsAuthenticated]


@pytest.mark.django_db
def test_course_detail(user_fixture, course_fixture):

    # GIVEN
    course = Course.objects.get()
    client = get_client(user_fixture)
    data_check = {
        "url": f"http://testserver/courses/courses/{course.id}", 
        "id": course.id,
        "title": course.title,
        "video_duration": course.video_duration,
        "language": course.language,
        "episodes": []
    }

    # WHEN
    request = client.get(values.COURSE_DETAIL_PATH)

    # THEN
    assert request.status_code == status.HTTP_200_OK
    assert request.data == data_check


@pytest.mark.django_db
def test_unauthenticated_user_cannot_access_courses_view(user_fixture):

    # GIVEN
    client = APIClient(user_fixture)

    # WHEN
    request = client.get(values.COURSES_LIST_PATH)

    # THEN
    assert request.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_create_course(user_fixture):
    
    # GIVEN
    client = get_client(user_fixture)
    data = values.DATA_NEW_COURSE
    
    # WHEN
    response = client.post(path=values.COURSES_LIST_PATH, data=data, format="json")
    
    # THEN
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == values.NEW_COURSE_RESPONSE


@pytest.mark.django_db
def test_list_curses(user_fixture, three_courses_fixture):

    # GIVEN
    client = get_client(user_fixture)

    # WHEN
    response = client.get(values.COURSES_LIST_PATH)

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.COURSES_RESPONSE


@pytest.mark.django_db
def test_update_course(user_fixture, course_fixture):

    # GIVEN
    client = get_client(user_fixture)
    new_data = values.DATA_CHANGED_COURSE

    # WHEN
    response = client.put(
        path=values.COURSE_DETAIL_PATH, 
        data=new_data, 
        format="json"
        )

    # THEN
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == values.COURSE_UPDATE_RESPONSE


@pytest.mark.django_db
def test_delete_course(user_fixture, course_fixture):

    # GIVEN
    client = get_client(user_fixture)

    # WHEN
    response = client.delete(path=values.COURSE_DETAIL_PATH)

    # THEN
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Course.objects.all().count() == 0


def test_episode_view_serialzier_class():
    assert EpisodeViewSet.serializer_class == EpisodeSerializer


def test_episode_view_permission_classes():
    assert EpisodeViewSet.permission_classes == [IsAuthenticated]
    

@pytest.mark.django_db
def test_episode_detail(user_fixture, episode_fixture):

    # GIVEN
    episode = Episode.objects.get()
    client = get_client(user_fixture)
    data_check = {
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
    assert request.data == data_check


@pytest.mark.django_db
def test_unauthenticated_user_cannot_access_episodes_view(user_fixture):

    # GIVEN
    client = APIClient(user_fixture)

    # WHEN
    request = client.get(values.EPISODES_LIST_PATH)

    # THEN
    assert request.status_code == status.HTTP_403_FORBIDDEN


# TODO
def test_create_episode():
    pass


def test_list_episodes():
    pass


def test_update_episode():
    pass


def test_delete_episode():
    pass
