# Generated by Django 4.2 on 2023-04-24 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0004_todolist_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='author',
        ),
    ]