import pytest
import re

from django.db.utils import DataError

from articles.models import Article


@pytest.mark.django_db
def test_article_model_raises_exception():
    # THEN
    with pytest.raises(DataError, match=re.escape("value too long for type character varying(150)")
        ):
        # WHEN
        Article.objects.create(title="test" * 150, content="test content")
