import pytest

from courses.tests import values
from .factories import CourseFactory, EpisodeFactory


@pytest.fixture
def course_fixture():
    return CourseFactory(id=values.COURSE_ID)


@pytest.fixture
def three_courses_fixture():
    text_fields = {
        "title": values.COURSE_TITLE,
        "video_duration": values.COURSE_VIDEO_DURATION,
        "language": values.COURSE_LANGUAGE
        }
    courses = [CourseFactory(id=id, **text_fields) for id in values.COURSES_IDS]
    return courses


@pytest.fixture
def episode_fixture():
    return EpisodeFactory(id=values.EPISODE_ID)
