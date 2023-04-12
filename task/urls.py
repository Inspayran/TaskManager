from django.urls import path

from task import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add_task/', views.add_task, name='add_task'),
    path('completed_task_list/', views.completed_task_list, name='completed'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/', views.delete_task, name='delete'),
    path('detail/<int:task_id>/', views.detail_task, name='detail'),
    path('update/<int:task_id>/', views.update_task, name='update'),
]