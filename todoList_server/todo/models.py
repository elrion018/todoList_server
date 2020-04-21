from django.db import models


class Project(models.Model):
    slug = models.AutoField(primary_key=True,
                            help_text='PK AutoIncrement')
    email = models.CharField(max_length=200, blank=False, null=True)
    project_text = models.CharField(max_length=200, blank=False, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_text


class ToDo(models.Model):
    slug = models.AutoField(primary_key=True,
                            help_text='PK AutoIncrement')
    email = models.CharField(max_length=200, blank=False, null=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=False)
    todo_text = models.CharField(max_length=200, blank=False, null=True)
    goal_date = models.DateTimeField(blank=False, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_text


class SubToDo(models.Model):
    slug = models.AutoField(primary_key=True, help_text='PK AutoIncrement')
    email = models.CharField(max_length=200, blank=False, null=True)
    todo = models.ForeignKey(
        ToDo, on_delete=models.CASCADE, null=True, blank=False)

    subtodo_text = models.CharField(max_length=200, blank=False, null=True)
    goal_date = models.DateTimeField(blank=False, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.subtodo_text
