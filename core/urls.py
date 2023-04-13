from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-list/', views.todo_list, name='todo-list'),
    path('todo-create/', views.todo_create, name='todo_create'),
    path('todo-edit/', views.todo_edit, name='todo_edit'),
    path('todo-delete/', views.todo_delete, name='todo_delete'),
]
