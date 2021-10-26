import pytest
import re

from django.db.utils import DataError

from articles.models import Article


@pytest.mark.django_db
def test_article_title_length_constraint():
    # THEN
    with pytest.raises(
        DataError, match=re.escape("value too long for type character varying(150)")
    ):

        # WHEN
        Article.objects.create(title="s" * 151, content="test content")
