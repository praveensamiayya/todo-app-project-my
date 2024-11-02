from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]