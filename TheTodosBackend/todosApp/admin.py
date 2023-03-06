from django.contrib import admin
from .models import TodoLists, TodoTasks

# # Register your models here.

# admin.site.register(Users)
admin.site.register(TodoLists)
admin.site.register(TodoTasks)