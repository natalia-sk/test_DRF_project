import pytest
import re

from django.db import models
from django.db.utils import DataError, IntegrityError

from courses.models import Episode
from courses.tests import values


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["max_length", "episode_data"],
    argvalues=[
        pytest.param(
            150,
            {"title": "t" * 151, "video_url": "www.test.pl"},
            id="too-long-title",
        ),
        pytest.param(
            200,
            {"title": "test title", "video_url": f"www.{'s' * 194}.pl"},
            id="too-long-video-url",
        ),
    ],
)
def test_episode_fields_max_length(course_fixture, max_length, episode_data):
    # THEN
    with pytest.raises(
        DataError,
        match=re.escape(f"value too long for type character varying({max_length})"),
    ):

        # WHEN
        Episode.objects.create(**episode_data, course_id=values.COURSE_ID)


@pytest.mark.django_db
def test_episode_model_without_course_raises_exception():
    # THEN
    with pytest.raises(
        IntegrityError,
        match='null value in column "course_id" violates not-null constraint',
    ):

        # WHEN
        Episode.objects.create()


def test_episode_model_fields():
    # GIVEN
    fields = Episode._meta.get_fields()
    fields_dict = {field.name: type(field) for field in fields}

    # THEN
    expected_data = {
        "id": models.AutoField,
        "title": models.CharField,
        "video_url": models.URLField,
        "course": models.ForeignKey,
        "notification": models.fields.reverse_related.ManyToOneRel,
    }

    assert fields_dict == expected_data
