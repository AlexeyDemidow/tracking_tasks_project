from django.contrib import admin
from django.urls import path, include

from tasks.API_views import TaskCreate, TaskStatusUpdate

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/tasks/', TaskCreate.as_view(), name='task-create'),
    path('api/tasks/<int:pk>/', TaskStatusUpdate.as_view(), name='get-task-and-status-update'),
]
