from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("latest/", views.latest),
    path("top/", views.top),
    path("post/<slug:slug>", views.post),
    path("create-post", views.create_post)
]

