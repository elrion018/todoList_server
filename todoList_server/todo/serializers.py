from rest_framework import serializers
from todo.models import Project, ToDo, SubToDo


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):

    project = ProjectSerializer(read_only=True)

    class Meta:
        model = ToDo
        fields = '__all__'


class SubToDoSerializer(serializers.ModelSerializer):

    todo = TodoSerializer(read_only=True)

    class Meta:
        model = SubToDo
        fields = '__all__'
