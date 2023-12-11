from collections.abc import Iterable
from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.contrib.auth.models import User


class Posts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    slug = models.SlugField(db_index=True, blank=True, max_length=250)
    title = models.CharField(max_length=250)
    author_img = models.CharField(max_length=50)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(default=datetime.now())
    content = models.TextField()
    
    def save(self, *args, **kwargs) :
        self.slug  = slugify(self.title)
        return super().save(*args, **kwargs)
    
    
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, db_index=True)
    password = models.CharField(max_length=250)
    post_count = models.IntegerField(default=0)