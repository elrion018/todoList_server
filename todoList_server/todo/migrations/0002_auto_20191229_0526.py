# Generated by Django 3.0 on 2019-12-29 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtodo',
            name='todo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.ToDo'),
        ),
    ]
