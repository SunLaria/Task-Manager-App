# Generated by Django 4.2.7 on 2024-01-22 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Manager_app', '0004_taskuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TaskUser',
        ),
    ]