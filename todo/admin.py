from django.contrib import admin
import reversion
from reversion.admin import VersionAdmin
# Register your models here.
from django.db import models
from . models import Task
admin.site.register(Task)
reversion.register(Task)

class TaskAdmin(VersionAdmin):
    pass
