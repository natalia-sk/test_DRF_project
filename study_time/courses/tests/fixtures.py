import pytest

from courses.tests import values
from .factories import CourseFactory, EpisodeFactory


@pytest.fixture
def course_fixture():
    return CourseFactory(
        id=values.COURSE_ID,
        title=values.COURSE_TITLE,
        video_duration=values.COURSE_VIDEO_DURATION,
        language=values.COURSE_LANGUAGE,
    )


@pytest.fixture
def three_courses_fixture(course_fixture):
    courses = [course_fixture]
    text_fields = {
        "title": values.COURSE_TITLE,
        "video_duration": values.COURSE_VIDEO_DURATION,
        "language": values.COURSE_LANGUAGE,
    }
    courses += [CourseFactory(id=id, **text_fields) for id in values.COURSES_IDS[1:]]
    return courses


@pytest.fixture
def episode_fixture(course_fixture):
    return EpisodeFactory(
        id=values.EPISODE_ID,
        title=values.EPISODE_TITLE,
        video_url = values.EPISODE_VIDEO_URL,
        course = course_fixture,
    )


@pytest.fixture
def three_episodes_fixture(episode_fixture, course_fixture):
    episodes = [episode_fixture]
    text_fields = {
        "title": values.EPISODE_TITLE,
        "video_url": values.EPISODE_VIDEO_URL}
    episodes += [EpisodeFactory(id=id, course=course_fixture, **text_fields) for id in values.EPISODES_IDS[1:]]
    return episodes
