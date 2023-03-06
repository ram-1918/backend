# Generated by Django 4.1.7 on 2023-02-24 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todosApp', '0004_remove_todolists_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolists',
            name='deadline',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='todotasks',
            name='deadline',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='todotasks',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
