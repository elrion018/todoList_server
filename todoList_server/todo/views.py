from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import ToDo, Project, SubToDo
from account.models import Account
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from todo.serializers import TodoSerializer, ProjectSerializer, SubToDoSerializer
from todoList_server.settings import SECRET_KEY
import jwt
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


@api_view(['POST'])
def project_list_related_email(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION', " ")
        user_token_info = jwt.decode(
            token, SECRET_KEY, algorithms='HS256')
        if Account.objects.filter(email=user_token_info['email']).exists():
            project_list = Project.objects.filter(
                email=user_token_info['email'])
            projectSerializer = ProjectSerializer(project_list, many=True)
    return Response(projectSerializer.data)


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


@api_view(["POST"])
def todo_list_related_project_email(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION', " ")
        user_token_info = jwt.decode(
            token, SECRET_KEY, algorithms='HS256')
        if Account.objects.filter(email=user_token_info['email']).exists():
            todo_list = ToDo.objects.filter(email=user_token_info['email'])
            todoSerializer = TodoSerializer(todo_list, many=True)
    return Response(todoSerializer.data)


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


@api_view(['GET', 'PUT', 'DELETE'])
def subtodo_detail(request, slug):
    try:
        subtodo = SubToDo.objects.get(slug=slug)

    except SubToDo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        subtodoSerializer = SubToDoSerializer(subtodo)
        return Response(subtodoSerializer.data)

    elif request.method == 'PUT':
        subtodoSerializer = SubToDoSerializer(subtodo, data=request.data)
        if subtodoSerializer.is_valid():
            subtodoSerializer.save()
            return Response(subtodoSerializer.data)
        return Response(subtodoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        subtodo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def subtodo_list(request):
    if request.method == 'GET':

        subtodo_list = SubToDo.objects.all()
        subtodoSerializer = SubToDoSerializer(subtodo_list, many=True)

        return Response(subtodoSerializer.data)

    elif request.method == 'POST':
        todo = ToDo.objects.get(slug=request.data['todo_id'])
        subtodoSerializer = SubToDoSerializer(data=request.data)
        if subtodoSerializer.is_valid():
            subtodo = subtodoSerializer.save()
            subtodo.todo = todo
            subtodo.save()
            return_serializer = SubToDoSerializer(subtodo)
            return Response(return_serializer.data, status=status.HTTP_201_CREATED)

        return Response(subtodoSerializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def todo_list_related_project_email(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION', " ")
        user_token_info = jwt.decode(
            token, SECRET_KEY, algorithms='HS256')
        if Account.objects.filter(email=user_token_info['email']).exists():
            todo_list = ToDo.objects.filter(email=user_token_info['email'])
            todoSerializer = TodoSerializer(todo_list, many=True)
    return Response(todoSerializer.data)


@api_view(["POST"])
def subtodo_list_related_project_email(request):
    if request.method == 'POST':
        token = request.META.get('HTTP_AUTHORIZATION', " ")
        user_token_info = jwt.decode(
            token, SECRET_KEY, algorithms='HS256')
        if Account.objects.filter(email=user_token_info['email']).exists():
            subtodo_list = SubToDo.objects.filter(
                email=user_token_info['email'])
            subtodoSerializer = SubToDoSerializer(subtodo_list, many=True)
    return Response(subtodoSerializer.data)
