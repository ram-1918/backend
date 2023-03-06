from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ReadPostView.as_view()),
    path('get/<int:pk>', views.UpdateDestroyView.as_view())
]
