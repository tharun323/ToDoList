# Generated by Django 2.0.4 on 2018-04-30 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='task',
        ),
    ]