import pytest
import re

from django.db.utils import DataError, IntegrityError
from courses.models import Episode
from courses.tests import values
from .factories import CourseFactory


@pytest.mark.django_db
def test_episode_model_too_long_title_raises_exception(course_fixture):

    # THEN
    with pytest.raises(
        DataError, 
        match=re.escape("value too long for type character varying(150)")
        ):

        # WHEN
        Episode.objects.create(title="s" * 151, video_url="www.test.pl", course_id=values.COURSE_ID)


@pytest.mark.django_db
def test_episode_model_too_long_video_url_raises_exception(course_fixture):

    # THEN
    with pytest.raises(
        DataError,
        match=re.escape("value too long for type character varying(200)")
        ):
        
        # WHEN
        Episode.objects.create(title="test title", video_url=f"www.{'s' * 194}.pl", course_id=values.COURSE_ID)


@pytest.mark.django_db
def test_episode_model_without_course_raises_exception():

    # THEN
    with pytest.raises(
        IntegrityError, 
        match='null value in column "course_id" violates not-null constraint'
        ):

        # WHEN
        Episode.objects.create(title="test title", video_url="www.test.pl")
