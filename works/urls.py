from django.urls import path
from works import views

app_name = 'works'

urlpatterns = [
    path('todo/', views.ToDoListView.as_view(), name="todo"),
    path('<int:work_id>/', views.ToDoListDetailView.as_view(), name="todo_detail"),
]