from django.db import models


class Project(models.Model):
    slug = models.AutoField(primary_key=True,
                            help_text='PK AutoIncrement')
<<<<<<< HEAD
    project_text = models.CharField(max_length=200, blank=False)
=======
    project_text = models.CharField(max_length=200, blank=False, null=True)
>>>>>>> 4fb737c2aef0863efd6f64318c6977664cf195ee
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_text


class ToDo(models.Model):
    slug = models.AutoField(primary_key=True,
                            help_text='PK AutoIncrement')
    project = models.ForeignKey(
<<<<<<< HEAD
        Project, on_delete=models.CASCADE, null=False, blank=False)
    todo_text = models.CharField(max_length=200, blank=False)
    goal_date = models.DateField(null=False, blank=False)
=======
        Project, on_delete=models.CASCADE, null=True, blank=False)
    todo_text = models.CharField(max_length=200, blank=False, null=True)
    goal_date = models.DateTimeField(blank=False, null=True)
>>>>>>> 4fb737c2aef0863efd6f64318c6977664cf195ee

    def __str__(self):
        return self.todo_text


class SubToDo(models.Model):
    slug = models.AutoField(primary_key=True, help_text='PK AutoIncrement')
    todo = models.ForeignKey(
        ToDo, on_delete=models.CASCADE, null=False, blank=False)
    subtodo_text = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.subtodo_text
