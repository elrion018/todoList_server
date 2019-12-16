from django.db import models


class Project(models.Model):
    slug = models.AutoField(primary_key=True,
                            help_text='PK AutoIncrement')
    project_text = models.CharField(max_length=200, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_text


class ToDo(models.Model):
    slug = models.AutoField(primary_key=True,
                            help_text='PK AutoIncrement')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True)
    todo_text = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.todo_text
