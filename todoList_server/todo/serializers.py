from rest_framework import serializers
from todo.models import Project, ToDo


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):

    project = ProjectSerializer(read_only=True)

    class Meta:
        model = ToDo
        fields = '__all__'
