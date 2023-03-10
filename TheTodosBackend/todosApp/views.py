from django.shortcuts import render
from .models import TodoLists, TodoTasks
from .serializers import  ListSerializer, TaskSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend # Filters module
from rest_framework import filters # Search Filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# class ListCreateUser(generics.ListCreateAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

# class RetrieveUpdateDestroyUser(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Users.objects.all()
#     serializer_class = UserSerializer

def test(request):
    tasks = TodoLists.objects.all()
    l = TodoTasks.objects.all()
    print("hey ypu")
    for j in l:
        print(j.list.pk, type(j.list.pk))
    print('---------')
    for i in tasks:
        print(i.name, i.id, type(i.id))
    return render(request)

class ListCreateTodoList(generics.ListCreateAPIView):
    queryset = TodoLists.objects.all()
    serializer_class = ListSerializer
    # filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # filterset_fields = ['name', 'priority', 'deadline', 'favorites']
    # search_fields = ['^name']# ['=name', '$name', '@name']
    # ordering_fields = ['name', 'priority', 'deadline']
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

class RetrieveUpdateDestroyTodoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoLists.objects.all()
    serializer_class = ListSerializer

class ListCreateTodoTask(generics.ListCreateAPIView):
    queryset = TodoTasks.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Retrieve the name parameter from the request
        list = self.request.query_params.get('list', None)

        # Filter the queryset based on the name parameter
        if list:
            # print(list)
            queryset = queryset.filter(list=list)

        return queryset

class RetrieveUpdateDestroyTodoTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoTasks.objects.all()
    serializer_class = TaskSerializer