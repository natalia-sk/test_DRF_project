from courses.serializers import EpisodeSerializer


def test_episode_serializer_contains_expected_fields():
    # GIVEN
    serializer = EpisodeSerializer()

    # WHEN
    serializer_fields = serializer.fields

    # THEN
    assert set(serializer_fields.keys()) == set(["url", "id", "title", "video_url", "course"])
