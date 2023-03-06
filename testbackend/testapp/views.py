from django.shortcuts import render
from rest_framework import generics
from testapp.models import TestModel
from testapp.serializers import TestSerializer

# Create your views here.

class ReadPostView(generics.ListCreateAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer

class UpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer
