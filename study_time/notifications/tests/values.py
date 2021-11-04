from django.urls import reverse

from courses.tests import values as course_values

NOTIFICATION_ID = 1
THREE_NOTIFICATIONS_IDS = [2, 3]
NOTIFICATIONS_IDS = [NOTIFICATION_ID] + THREE_NOTIFICATIONS_IDS

NOTIFICATION_DETAIL_PATH = reverse(
    "notification-detail", kwargs={"pk": NOTIFICATION_ID}
)
NOTIFICATIONS_LIST_PATH = reverse("notification-list")


# after using "three_courses_fixture"
NOTIFICATIONS_RESPONSE = {
    "count": 3,
    "next": None,
    "previous": None,
    "results": [
        {
            "id": notification_id,
            "title": f"New course: {course_values.COURSE_TITLE}",
            "body": f"Hey, there's a new course: {course_values.COURSE_TITLE} ({course_values.COURSE_VIDEO_DURATION}s)",
            "content_type": "Course",
            "article": None,
            "course": course_id,
            "episode": None,
        }
        for notification_id, course_id in zip(
            NOTIFICATIONS_IDS, course_values.COURSES_IDS
        )
    ],
}
