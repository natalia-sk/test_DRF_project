import pytest
from django.db.utils import DataError

from articles.models import Article
from courses.models import Course, Episode


@pytest.mark.django_db
def test_notification_signal_shorten_too_long_instance_title():
    try:
        course = Course.objects.create(
            title="c" * 150,
            video_duration=123,
            language="en",
        )
        Episode.objects.create(
            title="e" * 150,
            video_url="http://test.com",
            course_id=course.id,
        )
        Article.objects.create(
            title="a" * 150,
            content="test content",
        )
    except DataError as e:
        pytest.fail(f"Unexpected DataError: {e}...")
