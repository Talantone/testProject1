from django.urls import path, include
from . import views


app_name = 'tasks'

urlpatterns = [
    path('my_tasks/', views.TasksAPIList.as_view(), name='my_tasks'),
    path('my_tasks/<int:pk>/', views.TasksAPIUpdate.as_view()),
]