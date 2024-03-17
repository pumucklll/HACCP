import datetime
from django.views.generic import ListView
from .models import ToDoItem


class AllToDos(ListView):
    model = ToDoItem
    template_name = "index.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date__gte=datetime.date.today())

class TodayToDos(ListView):
    model = ToDoItem
    template_name = "today.html"

    def get_queryset(self):
        return ToDoItem.objects.filter(due_date=datetime.date.today())
