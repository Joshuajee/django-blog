# Generated by Django 4.2.7 on 2023-12-11 08:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0011_alter_author_email_alter_author_password_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="posts",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="posts",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 12, 11, 8, 41, 56, 926684)
            ),
        ),
    ]