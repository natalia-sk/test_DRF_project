from django.urls import reverse

# COURSES
COURSE_ID = 1

COURSES_IDS = [1, 2, 3]

COURSE_TITLE = "Some title, only for tests."
COURSE_VIDEO_DURATION = 123
COURSE_LANGUAGE = "en"

COURSE_DETAIL_PATH = reverse("course-detail", kwargs={"pk": COURSE_ID})
COURSES_LIST_PATH = reverse("course-list")

COURSES_RESPONSE = {
    "count": 3,
    "next": None,
    "previous": None,
    "results": [
        {
            "id": course_id,
            "title": COURSE_TITLE,
            "video_duration": COURSE_VIDEO_DURATION,
            "language": COURSE_LANGUAGE,
            "episodes": [],
        }
        for course_id in COURSES_IDS
    ],
}

DATA_NEW_COURSE = {
    "title": "test course title",
    "video_duration": 123,
    "language": "fr",
}

NEW_COURSE_RESPONSE = {"id": COURSE_ID, "episodes": [], **DATA_NEW_COURSE}

DATA_CHANGED_COURSE = {
    "title": "test new course title",
    "video_duration": 321,
    "language": "ru",
}

COURSE_UPDATE_RESPONSE = {"id": COURSE_ID, "episodes": [], **DATA_CHANGED_COURSE}

# EPISODES
EPISODE_ID = 1

EPISODES_IDS = [1, 2, 3]

EPISODE_TITLE = "Some title, only for tests."
EPISODE_VIDEO_URL = "http://test-episode-url.com"

EPISODE_DETAIL_PATH = reverse(
    "episode-detail", kwargs={"parent_lookup_course_id": COURSE_ID, "pk": EPISODE_ID}
)
EPISODES_LIST_PATH = reverse(
    "episode-list", kwargs={"parent_lookup_course_id": COURSE_ID}
)

EPISODES_RESPONSE = {
    "count": 3,
    "next": None,
    "previous": None,
    "results": [
        {
            "id": episode_id,
            "title": EPISODE_TITLE,
            "video_url": EPISODE_VIDEO_URL,
            "course": COURSE_ID,
        }
        for episode_id in EPISODES_IDS
    ],
}

DATA_NEW_EPISODE = {
    "title": "test episode title",
    "video_url": "http://test-episode.com",
    "course": COURSE_ID,
}

NEW_EPISODE_RESPONSE = {
    "id": EPISODE_ID,
    **DATA_NEW_EPISODE,
}

DATA_CHANGED_EPISODE = {
    "title": "test new episode title",
    "video_url": "http://test-brand-new-episode-url.com",
    "course": COURSE_ID + 1,
}

EPISODE_UPDATE_RESPONSE = {
    "id": EPISODE_ID,
    **DATA_CHANGED_EPISODE,
}
