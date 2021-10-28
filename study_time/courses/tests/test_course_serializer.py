from courses.serializers import CourseSerializer


def test_course_serializer_contains_expected_fields():
    # GIVEN
    serializer = CourseSerializer()

    # WHEN
    serializer_fields = serializer.fields

    # THEN
    assert set(serializer_fields.keys()) == set(
        ["id", "title", "video_duration", "language", "episodes"]
    )
