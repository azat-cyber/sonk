from django.shortcuts import render, redirect
from .models import Task, Image
from .forms import TaskForm, ImageForm


def index(request):
    tasks = Task.objects.order_by('-id')

    return render(request, 'main/index.html', {'title': 'Main Page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'ошибка'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def photo(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'main/Photos.html', {'form': form, 'img_obj': img_obj})
    else:
        photos = Image.objects.order_by('-id')
        form = ImageForm()
    return render(request, 'main/Photos.html', {'form': form, 'photos': photos})
