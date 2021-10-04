import pytest
import re

from django.db.utils import DataError
from courses.models import Course


@pytest.mark.django_db
def test_course_title_max_length():

    # THEN
    with pytest.raises(
        DataError, 
        match=re.escape("value too long for type character varying(150)")
        ):

        # WHEN
        Course.objects.create(title="s" * 151, video_duration=123, language="en")
