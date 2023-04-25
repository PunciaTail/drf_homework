from django.urls import path
from todo import views

urlpatterns = [
    path('list/', views.TodoView.as_view(), name='todo_view'),
]