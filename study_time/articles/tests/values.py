from django.urls import reverse


ARTICLE_ID = 1
THREE_ARTICLES_IDS = [2, 3]
ARTICLES_IDS = [ARTICLE_ID] + THREE_ARTICLES_IDS

ARTICLE_TITLE = "Some title, only for tests."
ARTICLE_CONTENT = "A little longer text, only for tests"

ARTICLE_DETAIL_PATH = reverse("articles-detail", kwargs={"pk": ARTICLE_ID})
ARTICLES_LIST_PATH = reverse("articles-list")

ARTICLES_RESPONSE = {
    "count": 3,
    "next": None,
    "previous": None,
    "results": [
        {"id": article_id, "title": ARTICLE_TITLE, "content": ARTICLE_CONTENT}
        for article_id in ARTICLES_IDS
    ],
}

DATA_NEW_ARTICLE = {"title": "test article title", "content": "test article content"}

NEW_ARTICLE_RESPONSE = {"id": ARTICLE_ID, **DATA_NEW_ARTICLE}

DATA_CHANGED_ARTICLE = {
    "title": "test new article title",
    "content": "test new article content",
}

ARTICLE_UPDATE_RESPONSE = {"id": ARTICLE_ID, **DATA_CHANGED_ARTICLE}
