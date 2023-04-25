from django.urls import path
from todo import views

urlpatterns = [
    path('list/', views.TodoView.as_view(), name='todo_view'),
    path('<int:todo_id>/', views.TodoDetailView.as_view(), name='todo_detail_view'),
]