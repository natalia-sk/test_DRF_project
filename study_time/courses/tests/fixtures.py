import pytest

from courses.tests import values
from .factories import CourseFactory


@pytest.fixture
def course_fixture():
    return CourseFactory(id=values.COURSE_ID)
