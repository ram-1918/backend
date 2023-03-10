from django.urls import path
from .views import CreatePost, UpdatePost


urlpatterns = [
    path("tutor-list", CreatePost.as_view()),
    path("tutor-list/<int:pk>", UpdatePost.as_view()),
]
