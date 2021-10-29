from notifications.serializers import NotificationSerializer


def test_notification_serializer_contains_expected_fields():
    # GIVEN
    serializer = NotificationSerializer()

    # WHEN
    serializer_fields = serializer.fields

    # THEN
    assert set(serializer_fields.keys()) == set(
        ["id", "title", "body", "content_type", "article", "course", "episode"]
    )

