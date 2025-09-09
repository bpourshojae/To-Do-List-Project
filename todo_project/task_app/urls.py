from django.urls import path
from . import views

app_name  = 'task_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.task_list, name='task_list'),
    path('edit/<int:id_>', views.edit_task, name='edit_task'),
    path('delete/<int:id_>', views.delete_task, name='delete_task'),
]
