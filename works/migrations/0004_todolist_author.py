# Generated by Django 4.2 on 2023-04-24 05:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('works', '0003_remove_todolist_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='work_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
