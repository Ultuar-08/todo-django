from django.contrib import admin
from django.urls import path
from todo_app.views import task_list, complete_task, delete_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_list, name='task_list'),
    path('complete/<int:task_id>/', complete_task, name='complete_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
]
