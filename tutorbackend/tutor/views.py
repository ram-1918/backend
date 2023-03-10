from django.shortcuts import render
from rest_framework import generics
from .models import TutorModel
from .serializers import TutorSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

class CreatePost(generics.ListCreateAPIView):
    queryset = TutorModel.objects.all()
    serializer_class = TutorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['question', 'answer', 'date_create', 'topic', 'student_name', 'company']
    search_fields = ['question', 'answer', 'topic', 'student_name', 'company']
    ordering_fields = ['topic', 'student_name', 'company']
    

class UpdatePost(generics.RetrieveUpdateDestroyAPIView):
    queryset = TutorModel.objects.all()
    serializer_class = TutorSerializer
