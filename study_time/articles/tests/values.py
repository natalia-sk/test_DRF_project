ARTICLE_ID = 1

ARTICLES_IDS = [i for i in range(1,4)]
ARTICLE_TITLE = "Some title, only for tests."
ARTICLE_CONTENT = "A little longer text, only for tests"

ARTICLES_RESPONSE = {
    "count": 3,
    "next": None, 
    "previous": None, 
    "results": [
        {"id": ARTICLES_IDS[0], "title": ARTICLE_TITLE, "content": ARTICLE_CONTENT}, 
        {"id": ARTICLES_IDS[1], "title": ARTICLE_TITLE, "content": ARTICLE_CONTENT}, 
        {"id": ARTICLES_IDS[2], "title": ARTICLE_TITLE, "content": ARTICLE_CONTENT}
        ]
    }
