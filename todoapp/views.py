# from django.shortcuts import render ,redirect
# from .models import todo
# # Create your views here.
# def home(request):
#     data = todo.objects.all()
#     return render(request,'home.html',{'data':data});

# def add(request):
#     tododata = request.POST['todo']
#     todo_item = todo(content =tododata)
#     todo_item.save()
#     return redirect(home)
# def deleteItem(request,todo_id):
#     item = todo.objects.get(id=todo_id)
#     item.delete()
#     return redirect(home)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Todo
from django.contrib.auth.decorators import login_required


# User Registration
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful! Please log in.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')


# User Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')


# User Logout
def user_logout(request):
    logout(request)
    return redirect('login')


# Home (ToDo List) - Protected Route
@login_required(login_url='login')
def home(request):
    data = Todo.objects.all()
    return render(request, 'home.html', {'data': data})


# Add ToDo Item - Protected Route
@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        tododata = request.POST.get('todo')
        if tododata:
            todo_item = Todo(content=tododata)
            todo_item.save()
    return redirect('home')


# Delete ToDo Item - Protected Route
@login_required(login_url='login')
def deleteItem(request, id):
    item = get_object_or_404(Todo, id=id)
    item.delete()
    messages.success(request, 'Task deleted successfully.')
    return redirect('home')
