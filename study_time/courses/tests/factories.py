from factory import django, Faker


class CourseFactory(django.DjangoModelFactory):
    class Meta:
        model = "courses.Course"

    title = Faker("sentence", nb_words=3)
    video_duration = Faker("random_int", min=1, max=999, step=1)
    language = Faker("random_element", elements=('en', 'ru', 'de', 'fr'))
