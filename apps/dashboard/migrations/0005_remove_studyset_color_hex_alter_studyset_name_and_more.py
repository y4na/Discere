# Generated by Django 5.1.3 on 2024-11-18 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studyset',
            name='color_hex',
        ),
        migrations.AlterField(
            model_name='studyset',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='studyset',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]
