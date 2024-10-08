from django.urls import path 
from .views import task_list, task_create, update_task, delete_task


urlpatterns = [
    path('all/', task_list, name='task_list'),
    path('add/', task_create, name='task_create'),
    path('edit/<int:pk>/', update_task, name='task_update'),
    path('delete/<int:pk>/', delete_task, name='task_delete')
]