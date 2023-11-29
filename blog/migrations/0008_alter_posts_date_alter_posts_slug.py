# Generated by Django 4.2.7 on 2023-11-24 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0007_alter_posts_date_alter_posts_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 24, 10, 3, 17, 441373)
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="slug",
            field=models.SlugField(blank=True, max_length=250),
        ),
    ]
