from rest_framework import serializers
from rest_framework.relations import HyperlinkedIdentityField
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
