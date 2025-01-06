from django.urls import path

from . import views
from .views import SignUpView

urlpatterns = [
    path('sign_up',  SignUpView.as_view(), name='register_page'),
    path('sign_in', views.SignInView.as_view(), name='login_page'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('todo/', views.ToDoListView.as_view(), name='todo'),
    path('edit/<int:task_id>/', views.ToDoEditView.as_view(), name='task_edit'),
    path('delete/<int:task_id>/', views.ToDoDeleteView.as_view(), name='task_delete'),
    path('', views.MainView.as_view(), name='main'),
]