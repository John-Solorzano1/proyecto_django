from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Project,Task
from .forms import CreateNewTask,CreateNewProject
# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request,'index.html',{
        'title': title
    })

def about(request):
    username = 'John'
    return render(request,'about.html',{
        'username': username
    })


def hello(request, username):
    return HttpResponse("<h2>Hello %s</h2>" % username)

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects' : projects
    })

def tasks(request):
    #task = Task.objects.get(title=title)
    task = Task.objects.all()
    return render(request, 'tasks/tasks.html',{
        'tasks':task
    })

def create_task(request):
    if request.method == 'GET':
         return render(request, 'tasks/create_task.html',
                  {'form': CreateNewTask()
                   })
    else:
        print(request.GET['title'])
        print(request.GET['description'])
        Task.objects.create(title = request.POST['title'], description = request.POST['descripcion'], projectKey=2)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
        'form': CreateNewProject()
        })
    else:
        Project.objects.create(name = request.POST["name"])
        redirect('projects')

def project_detail(request,id):
    print(id)
    return render(request, 'project/detail.html')