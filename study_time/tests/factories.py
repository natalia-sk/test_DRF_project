from django.contrib.auth.models import User
from factory import django


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = User
