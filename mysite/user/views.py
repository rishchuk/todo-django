from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.views import View

from .forms import UserRegistrationForm, ToDoForm, UserLoginForm
from .models import ToDo


class SignUpView(View):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if request.POST.getlist('check'):
            if form.is_valid():
                form.save()
                return redirect('login_page')
        return render(request, self.template_name, {'form': form})


# def signup(request):
#     form = UserRegistrationForm()
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#
#             return redirect('login_page')
#
#     context = {'form': form}
#     return render(request, 'user/register.html', context)

class SignInView(View):
    form_class = UserLoginForm
    template_name = 'user/login.html'

    def get(self, request):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)

                return redirect('todo')

        return render(request, self.template_name, {'error': 'Username or password is incorrect!', 'form': form})


# def login(request):
#     if request.method == 'POST':
#         user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
#         if user is not None:
#             auth.login(request, user)
#
#             return redirect('todo')
#         else:
#             return render(request, 'user/login.html', {'error': 'Username or password is incorrect!'})
#     else:
#         return render(request, 'user/login.html')

class Logout(View):
    def get(self, request):
        auth.logout(request)
        return redirect('login_page')


# def logout(request):
#     auth.logout(request)
#     return redirect('login_page')

class MainView(View):
    def get(self, request):
        return render(request, 'user/main.html')


# def test(request):
#     return render(request, 'user/main.html')


class ToDoListView(View):
    form_class = ToDoForm

    def get(self, request):
        task = self.form_class()
        status = request.GET.get('status')
        if status == 'completed':
            tasks = ToDo.objects.filter(user=request.user, status=1)
        elif status == 'active':
            tasks = ToDo.objects.filter(user=request.user, status=0)
        else:
            tasks = ToDo.objects.filter(user=request.user)

        context = {'tasks': tasks, 'task': task}
        return render(request, 'user/todo.html', context)

    def post(self, request):
        task = self.form_class(request.POST)
        if task.is_valid():
            task = task.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo')


class ToDoAddView(View):
    form_class = ToDoForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'user/todo.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('todo')


class ToDoEditView(View):
    def get(self, request, task_id):
        form = get_object_or_404(ToDo, id=task_id, user=request.user)
        if form.status:
            form.status = 0
        else:
            form.status = 1
        form.save()
        return redirect('todo')


class ToDoDeleteView(View):
    def get(self, request, task_id):
        form = get_object_or_404(ToDo, id=task_id, user=request.user)
        form.delete()
        return redirect('todo')

# def tasks_list(request):
#     if request.method == 'POST':
#         task = TaskForm(request.POST)
#
#         if task.is_valid():
#             task = task.save(commit=False)
#             task.user = request.user
#             task.save()
#             return redirect('todo')
#     else:
#         task = TaskForm()
#         tasks = Task.objects.filter(user=request.user)
#         context = {'tasks': tasks, 'task': task}
#         return render(request, 'user/todo.html', context)
#
#
# def add_task(request):
#     if request.method == 'POST':
#         task = TaskForm(request.POST)
#
#         if task.is_valid():
#             task = task.save(commit=False)
#             task.user = request.user
#             task.save()
#             return redirect('todo')
#     else:
#         task = TaskForm()
#     return render(request, 'user/todo.html', {'form': task})
#
#
# def task_edit(request, task_id):
#     task = get_object_or_404(Task, id=task_id, user=request.user)
#     if task.status:
#         task.status = 0
#     else:
#         task.status = 1
#     task.save()
#     return redirect('todo')
#
#
# def task_delete(request, task_id):
#     task = get_object_or_404(Task, id=task_id, user=request.user)
#     task.delete()
#     return redirect('todo')
