from django.urls import reverse

# COURSES
COURSE_ID = 1

COURSES_IDS = [i for i in range(1,4)]

COURSE_TITLE = "Some title, only for tests."
COURSE_VIDEO_DURATION = 123
COURSE_LANGUAGE = "en"

COURSE_TESTSERVER_URL = f"http://testserver/courses/courses/{COURSE_ID}"

COURSE_DETAIL_PATH = reverse("course-detail", kwargs={"pk": COURSE_ID})
COURSES_LIST_PATH = reverse("course-list")

COURSES_RESPONSE = {
    "count": 3, 
    "next": None, 
    "previous": None, 
    "results": [
        {"url": f"http://testserver/courses/courses/{course_id}",
        "id": course_id,
        "title": COURSE_TITLE,
        "video_duration": COURSE_VIDEO_DURATION,
        "language": COURSE_LANGUAGE,
        "episodes": []} for course_id in COURSES_IDS
    ]
}

DATA_NEW_COURSE = {
    "title": "test course title", 
    "video_duration": 123, 
    "language": "fr"
    }

NEW_COURSE_RESPONSE = {
    "id": COURSE_ID, 
    "url": COURSE_TESTSERVER_URL, 
    "episodes": [], 
    **DATA_NEW_COURSE
    }

DATA_CHANGED_COURSE = {
    "title": "test new course title", 
    "video_duration": 321,
    "language": "ru"
    }

COURSE_UPDATE_RESPONSE = {
    "id": COURSE_ID,
    "url": COURSE_TESTSERVER_URL,
    "episodes": [], 
    **DATA_CHANGED_COURSE
    }

# EPISODES
EPISODE_ID = 1

EPISODES_IDS = [i for i in range(1,4)]

EPISODE_TITLE = "Some title, only for tests."
EPISODE_VIDEO_URL = "http://test-episode-url.com"

EPISODE_TESTSERVER_URL = f"http://testserver/courses/episodes/{EPISODE_ID}"

EPISODE_DETAIL_PATH = reverse("episode-detail", kwargs={"pk": EPISODE_ID})
EPISODES_LIST_PATH = reverse("episode-list")

EPISODES_RESPONSE = {
    "count": 3, 
    "next": None, 
    "previous": None, 
    "results": [
        {"url": f"http://testserver/courses/episodes/{episode_id}",
        "id": episode_id,
        "title": EPISODE_TITLE,
        "video_url": EPISODE_VIDEO_URL,
        "course": course_id} for episode_id, course_id in zip(EPISODES_IDS, COURSES_IDS)
    ]
}

DATA_NEW_EPISODE = {
    "title": "test episode title",
    "video_url": "http://test-episode.com",
    "course": COURSE_ID
}

NEW_EPISODE_RESPONSE = {
    "id": EPISODE_ID,
    "url": EPISODE_TESTSERVER_URL,
    **DATA_NEW_EPISODE
}

DATA_CHANGED_EPISODE = {
    "title": "test new episode title",
    "video_url": "http://test-brand-new-episode-url.com",
    "course": COURSE_ID + 1
}

EPISODE_UPDATE_RESPONSE = {
    "id": EPISODE_ID,
    "url": EPISODE_TESTSERVER_URL,
    **DATA_CHANGED_EPISODE
}
