# Generated by Django 4.1.7 on 2023-02-23 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todosApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todotasks',
            name='list',
        ),
        migrations.DeleteModel(
            name='TodoLists',
        ),
        migrations.DeleteModel(
            name='TodoTasks',
        ),
    ]