# Generated by Django 3.2.6 on 2021-10-28 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_alter_course_language"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={"ordering": ["id"]},
        ),
        migrations.AlterModelOptions(
            name="episode",
            options={"ordering": ["id"]},
        ),
    ]