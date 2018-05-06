from django.urls import path

from . import views

app_name='todo'

urlpatterns=[
    path('',views.Home,name='Home'),
    path('<int:id>/',views.delete,name='delete'),
    path('today/',views.filtertoday,name='today'),
    path('week/',views.filterweek,name='week'),
    path('nweek/',views.filternextweek,name='nweek'),
    path('overdue/',views.filteroverdue,name='overdue'),

]
