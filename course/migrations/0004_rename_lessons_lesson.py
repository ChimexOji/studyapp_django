# Generated by Django 4.1 on 2022-09-29 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_lessons'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Lessons',
            new_name='Lesson',
        ),
    ]
