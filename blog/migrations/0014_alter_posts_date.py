# Generated by Django 4.2.7 on 2023-12-11 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0013_alter_posts_author_alter_posts_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 11, 8, 44, 21, 860999)
            ),
        ),
    ]
