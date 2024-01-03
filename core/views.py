from django.shortcuts import render, redirect
from core.models import TodoTask
from core.forms import CreateTaskForm

def index(request):
    todo_tasks = TodoTask.objects.filter(
        deleted=False
        ).order_by('-update_date')
    return render(
        request,
        'core/index.html', 
        {
            'todo_tasks': todo_tasks,
            'status': 'All'
        }
    )

def create_task(request):
    form = CreateTaskForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        TodoTask.objects.create(title=title)
        
    return redirect('index')
    
    
def complete_task(request, task_id):
    task = TodoTask.objects.get(pk=task_id)
    task.completed = True 
    task.save()
    
    return redirect('index')

def delete_task(request, task_id):
    task = TodoTask.objects.get(pk=task_id)
    task.deleted = True 
    task.save()
    
    return redirect('index')

def retrieve_finished_tasks(request):
    finished_tasks = TodoTask.objects.filter(
        completed=True,
        deleted=False
    ).order_by('-update_date')
    return render(
        request,
        'core/index.html',
        {'todo_tasks': finished_tasks, 'status': 'finished'}
    )


def retrieve_unfinished_tasks(request):
    unfinished_tasks = TodoTask.objects.filter(
        completed=False,
        deleted=False
    ).order_by('-update_date')
    return render(
        request,
        'core/index.html',
        {'todo_tasks': unfinished_tasks, 'status': 'unfinished'}
    )


def retrieve_delete_tasks(request):
    deleted_tasks = TodoTask.objects.filter(
        deleted=True
    ).order_by('-update_date')
    return render(
        request,
        'core/index.html',
        {'todo_tasks': deleted_tasks, 'status': 'deleted'}
    )