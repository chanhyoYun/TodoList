# Generated by Django 4.2 on 2023-04-24 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0002_alter_todolist_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='author',
        ),
    ]