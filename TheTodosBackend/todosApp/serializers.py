from rest_framework import serializers
from .models import TodoLists, TodoTasks

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoTasks
        fields = '__all__'

class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(read_only = True, many = True)
    class Meta:
        model = TodoLists
        fields = '__all__'

        