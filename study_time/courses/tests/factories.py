from factory import django, Faker, SubFactory
from utils.constants import LanguagesChoices


class CourseFactory(django.DjangoModelFactory):
    class Meta:
        model = "courses.Course"

    title = Faker("sentence", nb_words=3)
    video_duration = Faker("random_int", min=1, max=999, step=1)
    language = Faker("random_element", elements=(LanguagesChoices.values))


class EpisodeFactory(django.DjangoModelFactory):
    class Meta:
        model = "courses.Episode"

    title = Faker("sentence", nb_words=3)
    video_url = Faker("url")
    course = SubFactory(CourseFactory)
