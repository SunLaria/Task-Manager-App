# Generated by Django 4.2.7 on 2024-01-22 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Task_Manager_app', '0011_remove_category_user_remove_task_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Category',
        ),
        migrations.AddField(
            model_name='task',
            name='Category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Task_Manager_app.category'),
            preserve_default=False,
        ),
    ]
