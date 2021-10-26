import pytest

from articles.tests.factories import ArticleFactory
from notifications.models import Notification
from courses.tests.factories import CourseFactory, EpisodeFactory


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["instance_title", "expected_notification_title"],
    argvalues=[
        pytest.param(
            "e" * 150,
            f"New article: {'e'*100}...",
            id="title-longer-than-100-characters",
        ),
        pytest.param(
            "e" * 100,
            f"New article: {'e'*100}",
            id="title-max-100-characters",
        ),
    ],
)
def test_notification_signal_article(instance_title, expected_notification_title):
    # GIVEN
    ArticleFactory(title=instance_title)
    notification = Notification.objects.get()

    # THEN
    assert notification.title == expected_notification_title
    assert notification.body == f"Hey, there's a new article: {instance_title}"
    assert notification.content_type == "Article"
    assert Notification.objects.all().count() == 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["instance_title", "expected_notification_title"],
    argvalues=[
        pytest.param(
            "e" * 150,
            f"New course: {'e'*100}...",
            id="title-longer-than-100-characters",
        ),
        pytest.param(
            "e" * 100,
            f"New course: {'e'*100}",
            id="title-max-100-characters",
        ),
    ],
)
def test_notification_signals_course(instance_title, expected_notification_title):
    # GIVEN
    instance = CourseFactory(title=instance_title)
    notification = Notification.objects.get()

    # THEN
    assert notification.title == expected_notification_title
    assert (
        notification.body
        == f"Hey, there's a new course: {instance_title} ({instance.video_duration}s)"
    )
    assert notification.content_type == "Course"
    assert Notification.objects.all().count() == 1


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["instance_title", "expected_notification_title"],
    argvalues=[
        pytest.param(
            "e" * 150,
            f"New episode: {'e'*100}...",
            id="title-longer-than-100-characters",
        ),
        pytest.param(
            "e" * 100,
            f"New episode: {'e'*100}",
            id="title-max-100-characters",
        ),
    ],
)
def test_notification_signals_episode(instance_title, expected_notification_title):
    # GIVEN
    instance = EpisodeFactory(title=instance_title)
    notification = Notification.objects.all()[1]

    # THEN
    assert notification.title == expected_notification_title
    assert (
        notification.body
        == f"Hey, there's a new episode: {instance_title} (in {instance.course.title} course)"
    )
    assert notification.content_type == "Episode"
    assert Notification.objects.all().count() == 2
