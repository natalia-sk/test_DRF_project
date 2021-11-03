import pytest
import re

from django.db import models
from django.db.utils import DataError, IntegrityError

from courses.models import Course
from courses.tests import values


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["max_length", "course_data"],
    argvalues=[
        pytest.param(
            150,
            {"title": "t" * 151, "video_duration": 123, "language": "en"},
            id="too-long-title",
        ),
        pytest.param(
            10,
            {"title": "test title", "video_duration": 123, "language": "l" * 11},
            id="too-long-language",
        ),
    ],
)
def test_course_fields_max_length(max_length, course_data):
    # THEN
    with pytest.raises(
        DataError,
        match=re.escape(f"value too long for type character varying({max_length})"),
    ):

        # WHEN
        Course.objects.create(**course_data)


@pytest.mark.django_db()
def test_course_language_default_value():
    # WHEN
    course = Course.objects.create(
        title=values.COURSE_TITLE, video_duration=values.COURSE_VIDEO_DURATION
    )

    # THEN
    assert course.language == "en"


@pytest.mark.django_db
def test_course_video_duration_not_null():
    # THEN
    with pytest.raises(
        IntegrityError,
        match='null value in column "video_duration" violates not-null constraint',
    ):

        # WHEN
        Course.objects.create()


def test_course_model_fields():
    # GIVEN
    fields = Course._meta.get_fields()
    fields_dict = {field.name: type(field) for field in fields}

    # THEN
    expected_data = {
        "id": models.AutoField,
        "title": models.CharField,
        "video_duration": models.PositiveIntegerField,
        "language": models.CharField,
        "episodes": models.ManyToOneRel,
        "notification": models.ManyToOneRel,
    }

    assert fields_dict == expected_data
