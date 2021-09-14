from articles.serializers import ArticleSerializer


def test_serializer_contains_expected_fields():
    # GIVEN
    serializer = ArticleSerializer()
    # WHEN
    serializer_fields = serializer.fields
    # THEN
    assert set(serializer_fields.keys()) == set(['id', 'title', 'content'])
