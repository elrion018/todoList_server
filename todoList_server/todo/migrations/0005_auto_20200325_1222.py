# Generated by Django 3.0 on 2020-03-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20200319_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtodo',
            name='subtodo_text',
            field=models.CharField(max_length=200, null=True),
        ),
    ]