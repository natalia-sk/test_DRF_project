import pytest
import re

from django.db import models
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


def test_article_model_fields():
    # GIVEN
    fields = Article._meta.get_fields()
    fields_dict = {field.name: type(field) for field in fields}

    # THEN
    expected_data = {
        "id": models.AutoField,
        "title": models.CharField,
        "content": models.TextField,
        "notification": models.ManyToOneRel,
    }

    assert fields_dict == expected_data
