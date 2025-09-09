from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.

def index(request):
    task_form = TaskForm()
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('task_app:task_list')
    
    return render(request,'task_app/index.html',{'form':task_form})

def task_list(request):
    taskslist = Task.objects.all()
    return render(request,'task_app/task_list.html',{'taskslist':taskslist})

def edit_task(request,id_):
    task = get_object_or_404(Task,id=id_)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('task_app:task_list')
    else:
        task_form = TaskForm(instance=task)

    return render(request, 'task_app/edit_task.html', {'form': task_form,'task':task})    

def delete_task(request,id_):
    task = get_object_or_404(Task,id=id_)
    if request.method == "POST":
        
            task.delete()
            return redirect('task_app:task_list')
    else:
        # task_form = TaskForm(instance=task)
        return render(request,'task_app/delete_task_confirm.html',{'task':task})