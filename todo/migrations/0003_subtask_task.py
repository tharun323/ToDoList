# Generated by Django 2.0.4 on 2018-04-30 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_remove_subtask_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.Task'),
        ),
    ]
