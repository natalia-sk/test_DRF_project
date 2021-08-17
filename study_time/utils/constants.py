from django.db.models import TextChoices


class LanguagesChoices(TextChoices):
    EN = "English"
    RU = "Russian"
    DE = "German"
    FR = "French"
