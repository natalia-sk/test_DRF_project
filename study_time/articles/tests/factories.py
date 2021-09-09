from factory import django, Faker


class ArticleFactory(django.DjangoModelFactory):
    class Meta:
        model = "articles.Article"

    title = Faker("sentence", nb_words=3)
    content = Faker("paragraph")
