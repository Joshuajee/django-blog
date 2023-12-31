from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("latest/", views.latest),
    path("top/", views.top),
    path("post/<slug:slug>", views.post),
    path("create-post", views.create_post),
    path("my-blogs/", views.my_post),
    path("profile/", views.my_profile),
    path("profile/upload", views.upload_profile_img),
    path("signup/", views.signup),
    path("login/", views.login_view),
    path("logout/", views.logout_view)
] 


