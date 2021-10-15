import pytest

from articles.tests.factories import ArticleFactory
from notifications.models import Notification


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
