# Generated by Django 4.1.7 on 2023-02-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todosApp', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolists',
            name='count',
        ),
    ]