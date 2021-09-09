import pytest

from .factories import UserFactory


@pytest.fixture
def user_fixture():
    return UserFactory()
