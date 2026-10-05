from django.shortcuts import render
from .models import Task


def task_list(request):
    tasks = Task.objects.all()
    #Task.objects.create(title='New Task', completed=False)
    return render(request, 'task_list.html', {
        'tasks': tasks
    })