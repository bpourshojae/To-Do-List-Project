from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from .models import Task
from .forms import UserForm, UserProfileInfo
from django.contrib.auth.models import User

from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task=task_form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_app:task_list')
    else:
        task_form = TaskForm()
    return render(request,'task_app/index.html',{'form':task_form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('task_app:index'))
@login_required
def task_list(request):
    taskslist = Task.objects.filter(user=request.user)
    return render(request,'task_app/task_list.html',{'taskslist':taskslist})

def edit_task(request,id_):
    task = get_object_or_404(Task,id=id_)
    if request.method == "POST":
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task=task_form.save(commit=False)
            task.user = request.user
            task.save()
            login(request.user)
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
    
def register_user(request):
    if request.method == "POST":
        User_Form = UserForm(request.POST)
        User_profile_form = UserProfileInfo(request.POST)
        if User_Form.is_valid() and User_profile_form.is_valid():
            user = User_Form.save(commit=False)
            user.set_password(user.password)
            user.save()
            
            profile = User_profile_form.save(commit=False)
            profile.user = user
            
            if ('profile_pic' in request.FILES):
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            return redirect('task_app:task_list')    
    else:        
        User_Form = UserForm()
        User_profile_form = UserProfileInfo()
    # User_profile_form.user = User_Form
    return render(request,'task_app/registration.html',{'profile_form':User_profile_form,'user_form':User_Form})

def user_login(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('task_app:task_list'))
            else:
                return HttpResponse('Account Not Active')   
        else:
            print("Some tried to login and failed") 
            return HttpResponse("Invalid Login detail")
    else:
        return render(request,'task_app/login.html',{})
