from django.db import models

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

# Create your models here

class Task(models.Model):
    COMPLETED='COMPLETED'
    PENDING='PENDING'
    STATE_CHOICES=(
        (COMPLETED,'COMPLETED'),
        (PENDING,'PENDING'),
    )
    title=models.CharField(max_length=200)
    due_date=models.DateTimeField(blank=True,null=True)
    state=models.CharField(max_length=10,choices=STATE_CHOICES,default=PENDING)


    def __str__(self):
        return self.title
