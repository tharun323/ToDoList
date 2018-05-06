from django import forms

from . models import Task
class TodoForm(forms.ModelForm):
    title=forms.CharField(label="Task",widget=forms.TextInput(attrs={'placeholder': 'Enter Task Title'}))
    due_date=forms.DateTimeField(label="Date",widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    class Meta:
        model=Task
        fields=('title','due_date','state')

