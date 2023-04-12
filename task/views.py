from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks_list = Task.objects.filter(completed=False)
    paginator = Paginator(tasks_list, 3)

    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)

    context = {
        'tasks': tasks,
    }
    return render(request, 'main.html', context)


def completed_task_list(request):
    tasks = Task.objects.filter(completed=True)
    context = {
        'tasks': tasks,
    }
    return render(request, 'completed_task_list.html', context)


def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        task = Task(title=title, description=description)
        task.save()
    return redirect('task_list')


def detail_task(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'task': task}
    return render(request, 'task_detail.html', context)


def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.completed = True
        task.completed_at = datetime.now()
        task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)

    if request.method == 'POST':
        task.delete()
    return redirect('task_list')


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        form.save()
        return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'main.html', context)

