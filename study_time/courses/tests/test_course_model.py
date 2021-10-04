import pytest
import re

from django.db.utils import DataError, IntegrityError
from courses.models import Course
from courses.tests import values


@pytest.mark.django_db
def test_course_title_max_length():

    # THEN
    with pytest.raises(
        DataError, 
        match=re.escape("value too long for type character varying(150)")
        ):

        # WHEN
        Course.objects.create(title="s" * 151, video_duration=123, language="en")


@pytest.mark.django_db()
def test_course_language_default_value():

    # WHEN
    course = Course.objects.create(title=values.COURSE_TITLE, video_duration=values.COURSE_VIDEO_DURATION)

    # THEN
    assert course.language == "en"


@pytest.mark.django_db
def test_course_video_duration_not_null():
    
    # THEN
    with pytest.raises(
        IntegrityError, 
        match='null value in column "video_duration" violates not-null constraint'
        ):

        # WHEN
        Course.objects.create()
