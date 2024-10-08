from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


# Create your views here.

def task_list(request): 
    tasks = Task.objects.all() 
    return render(request, 'todo/task_list.html', {'tasks':tasks})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form})


def task_update(request, pk):
    task = Task.objects.get(pk=pk)  
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        # return redirect('/task/alll') 
        return redirect('task_list') # Почему этот метод лучше ? 
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

