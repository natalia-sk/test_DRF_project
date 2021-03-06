# Generated by Django 3.2.6 on 2021-08-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0002_auto_20210817_1447"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="language",
            field=models.CharField(
                choices=[
                    ("en", "English"),
                    ("ru", "Russian"),
                    ("de", "German"),
                    ("fr", "French"),
                ],
                default="en",
                max_length=10,
            ),
        ),
    ]
