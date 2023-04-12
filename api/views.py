from django.shortcuts import render

from task.models import Task
from .serializers import TaskSerializer
from rest_framework import generics, viewsets


class TaskSerializerView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer