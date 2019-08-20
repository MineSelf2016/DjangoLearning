from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:blog_id>/detail", views.detail, name = "detail"),
    path("<int:blog_id>/modify", views.modify, name = "modify"),
    path("hello_world", views.hello_world, name = "hello_world"),
]

