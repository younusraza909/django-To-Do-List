from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Todo
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    tasks = Todo.objects.order_by("-added_date")
    context={
        "tasks":tasks
    }
    return render(request,"main/index.html",context)


def addTask(request):
    if request.method == "POST":
        task=request.POST["task"]
        added_time=datetime.now()
        if task:
            task=Todo(added_date=added_time,task=task)
            task.save()
            return HttpResponseRedirect("/")


def delete(request,task_id):
    instance=Todo.objects.filter(id=task_id)
    instance.delete()
    return HttpResponseRedirect("/")
