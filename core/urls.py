from django.urls import path
from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_task', views.create_task, name='create_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
    path('complete_task/<int:task_id>', views.complete_task, name='complete_task'),
    path('finished_tasks', views.retrieve_finished_tasks, name='finished_tasks'),
    path('unfinished_tasks', views.retrieve_unfinished_tasks, name='unfinished_tasks'),
    path('deleted_tasks', views.retrieve_delete_tasks, name='deleted_tasks')
]