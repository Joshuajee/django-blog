# Generated by Django 4.2.7 on 2023-11-29 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0008_alter_posts_date_alter_posts_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 29, 10, 1, 55, 559888)
            ),
        ),
    ]
