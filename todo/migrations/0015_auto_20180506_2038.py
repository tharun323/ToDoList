# Generated by Django 2.0.4 on 2018-05-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_auto_20180506_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default=False, max_length=200),
        ),
    ]
