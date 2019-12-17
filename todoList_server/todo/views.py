from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import ToDo, Project
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from todo.serializers import TodoSerializer, ProjectSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def project_list(request):

    if request.method == 'GET':
        project_list = Project.objects.all()
        projectSerializer = ProjectSerializer(project_list, many=True)

        return Response(projectSerializer.data)

    elif request.method == 'POST':
        projectSerializer = ProjectSerializer(data=request.data)
        if projectSerializer.is_valid():
            projectSerializer.save()

            return Response(projectSerializer.data, status=status.HTTP_201_CREATED)

        return Response(projectSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, slug):

    try:
        project = Project.objects.get(slug=slug)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        projectSerializer = ProjectSerializer(project)
        return Response(projectSerializer.data)

    elif request.method == 'PUT':
        projectSerializer = ProjectSerializer(project, data=request.data)
        if projectSerializer.is_valid():
            projectSerializer.save()
            return Response(projectSerializer.data)
        return Response(projectSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def todo_list(request):
    print("call")
    if request.method == 'GET':

        todo_list = ToDo.objects.all()
        todoSerializer = TodoSerializer(todo_list, many=True)

        return Response(todoSerializer.data)

    elif request.method == 'POST':
        project = Project.objects.get(slug=request.data['project_id'])
        todoSerializer = TodoSerializer(data=request.data)
        if todoSerializer.is_valid():
            todo = todoSerializer.save()
            todo.project = project
            todo.save()
            return_serializer = TodoSerializer(todo)
            return Response(return_serializer.data, status=status.HTTP_201_CREATED)
        return Response(todoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def todo_list_related_project(request, slug):
    if request.method == 'GET':
        project = Project.objects.get(slug=slug)
        todo_list = project.todo_set.all()
        todoSerializer = TodoSerializer(todo_list, many=True)

        return Response(todoSerializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, slug):
    try:
        todo = ToDo.objects.get(slug=slug)
    except ToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        todoSerializer = TodoSerializer(todo)
        return Response(todoSerializer.data)

    elif request.method == 'PUT':
        todoSerializer = TodoSerializer(todo, data=request.data)
        if todoSerializer.is_valid():
            todoSerializer.save()
            return Response(todoSerializer.data)
        return Response(todoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)