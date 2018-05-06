# Generated by Django 2.0.4 on 2018-04-30 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20180430_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='choice',
        ),
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('C', 'COMPLETED'), ('P', 'PENDING')], default='P', max_length=1),
        ),
    ]
