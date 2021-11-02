import pytest
import re

from django.db import models
from django.db.utils import DataError

from notifications.models import Notification


@pytest.mark.django_db
@pytest.mark.parametrize(
    argnames=["max_length", "notification_data"],
    argvalues=[
        pytest.param(120, {"title": "t" * 121}, id="too-long-title"),
        pytest.param(10, {"content_type": "c" * 11}, id="too-long-content-type"),
    ],
)
def test_notification_fields_max_length(max_length, notification_data):
    # THEN
    with pytest.raises(
        DataError,
        match=re.escape(f"value too long for type character varying({max_length})"),
    ):

        # WHEN
        Notification.objects.create(**notification_data)


def test_notification_model_fields():
    # GIVEN
    fields = Notification._meta.get_fields()
    fields_dict = {field.name: type(field) for field in fields}

    # THEN
    expected_data = {
        "id": models.AutoField,
        "title": models.CharField,
        "body": models.TextField,
        "content_type": models.CharField,
        "article": models.ForeignKey,
        "course": models.ForeignKey,
        "episode": models.ForeignKey,
    }

    assert fields_dict == expected_data
