from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('project', views.project_list, name='project_list'),
    path('project/email', views.project_list_related_email, name='project_email')
    path('project/<int:slug>', views.project_detail, name='project_detail'),
    path('todo', views.todo_list, name="todo_list"),
    path('todo/<int:slug>', views.todo_detail, name='todo_detail'),
    path('todo/related_project/<int:slug>',
         views.todo_list_related_project, name="todo_list_related_project"),
    path('subtodo', views.subtodo_list, name="todo_list"),
    path('subtodo/<int:slug>', views.subtodo_detail, name='subtodo_detail')
]
