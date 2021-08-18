from django.db.models import TextChoices


class LanguagesChoices(TextChoices):
    ENGLISH = ("en", "English")
    RUSSIAN = ("ru", "Russian")
    GERMAN = ("de", "German")
    FRENCH = ("fr", "French")
