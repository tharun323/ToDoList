from django.test import TestCase
from todo.models import Task
from django.utils import timezone
from django.urls import reverse
from todo.forms import TodoForm
from todo.views import Home

#tesing djnago models
class ToDoModelTest(TestCase):

    def CreateTask(self,title="watch today",due_date="2018-02-02"):
        return Task.objects.create(title=title, due_date=due_date)

    def TestCreateTask(self):
        w=self.CreateTask()
        self.assertTrue(isinstance(w,Task))
        self.assertEqual(w.__unicode__(),w.title)
#End of django models Testing.................................

#testing views .................................................
    def TestHomeView(self):
        w=self.CreateTask()
        url=reverse('Home')
        resp=self.client.get(url)

        self.assertEqual(resp.status_code,200)
        self.assertIn(w.title,resp.content)

    def TestdeleteView(self):
        w = self.CreateTask()
        url = reverse('delete')
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(w.title, resp.content)

   def TestmonthView(self):
        w=self.CreateTask()
        url=reverse('nweek')
        resp=self.client.get(url)

        self.assertEqual(resp.status_code,200)
        self.assertIn(w.title,resp.content)

   def TesttodayView(self):
        w=self.CreateTask()
        url=reverse('today')
        resp=self.client.get(url)

        self.assertEqual(resp.status_code,200)
        self.assertIn(w.title,resp.content)

   def TestweekView(self):
        w=self.CreateTask()
        url=reverse('week')
        resp=self.client.get(url)

        self.assertEqual(resp.status_code,200)
        self.assertIn(w.title,resp.content)
#testing views completed.......................................

