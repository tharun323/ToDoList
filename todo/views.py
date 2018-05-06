from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from . forms import TodoForm
from . models import Task
from django.db.models import Q
from datetime import datetime,timedelta,date
from django.utils import timezone
import pytz

def Home(request):
    query = request.GET.get("q")
    form = TodoForm(request.POST)
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            t = form.save(commit=False)
            title=form.cleaned_data['title']
            due_date=form.cleaned_data['due_date']
            t=Task(title=title,due_date=due_date)
            t.save()
    else:
        form=TodoForm()
    p = Task.objects.order_by('due_date').all()
    if query:
        p= p.filter(title__icontains=query)
    return render(request,'todo/Home.html',{'form':form,'alltasks':p,})


def delete(request,id):
    todelete=get_object_or_404(Task,pk=id).delete()
    return HttpResponse("deleted")

def filtertoday(request):
    td=datetime.today()
    res=Task.objects.filter(due_date__date=td)
    return render(request,'todo/today.html',{'res':res})

def filterweek(request):
    td=datetime.today()
    week=td+timedelta(days=7)
    res=Task.objects.filter(due_date__range=[td,week])
    return render(request,'todo/week.html',{'res':res})


def filternextweek(request):
    td = datetime.today()
    week = td + timedelta(days=7)
    nweek=week+timedelta(days=7)
    res=Task.objects.filter(due_date__range=[week,nweek])
    return render(request,'todo/month.html',{'res':res})


def filteroverdue(request):
    td = datetime.today()
    week = td + timedelta(days=7)
    nweek=week+timedelta(days=7)
    res=Task.objects.filter(due_date__gte=nweek)
    return render(request,'todo/month.html',{'res':res})

