# Generated by Django 5.1.3 on 2024-11-18 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_studyset_color_studyset_description_studyset_subject_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='StudySet',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
