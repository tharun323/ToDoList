# Generated by Django 2.0.4 on 2018-05-06 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20180430_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='task',
        ),
        migrations.DeleteModel(
            name='SubTask',
        ),
    ]
