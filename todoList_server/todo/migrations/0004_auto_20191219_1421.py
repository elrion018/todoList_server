# Generated by Django 3.0 on 2019-12-19 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20191219_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='goal_date',
            field=models.DateTimeField(null=True),
        ),
    ]
