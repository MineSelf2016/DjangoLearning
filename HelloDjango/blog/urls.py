from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:blog_id>/content", views.content, name = "content"),
    path("<int:blog_id>/modify", views.modify, name = "modify"),
    path("hello_world", views.hello_world, name = "hello_world"),
]