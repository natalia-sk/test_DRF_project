from django.urls import reverse

COURSE_ID = 1

COURSES_IDS = [i for i in range(1,4)]

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
    "url": f"http://testserver/courses/courses/{COURSE_ID}", 
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
    "url": f"http://testserver/courses/courses/{COURSE_ID}",
    "episodes": [], 
    **DATA_CHANGED_COURSE
    }
