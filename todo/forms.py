from django import forms

from . models import Task
class TodoForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=('title','due_date','state')

