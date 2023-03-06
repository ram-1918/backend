from django.urls import path
from . import views

urlpatterns = [
    # path('users/', views.ListCreateUser.as_view()),
    # path('users/<int:pk>', views.RetrieveUpdateDestroyUser.as_view()),
    path('test/', views.test),
    path('lists/', views.ListCreateTodoList.as_view()),
    path('lists/<int:pk>', views.RetrieveUpdateDestroyTodoList.as_view()),

    path('tasks/', views.ListCreateTodoTask.as_view()),
    path('tasks/<int:pk>', views.RetrieveUpdateDestroyTodoTask.as_view()),

]
