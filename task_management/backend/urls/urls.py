from django.urls import path
from backend.views.user_views import UserView
from backend.views.task_views import TaskView

urlpatterns = [
    path('user', UserView.as_view(), name="user view"), # end point for creating user
    path('create/', TaskView.as_view(), name = "create-task"), # end point for creating a task
    path('assign/', TaskView.as_view(), name = "assign-task"), # end point for assigning a task to a user
    path('get-task/', TaskView.as_view(), name = "fetch-task-info"), # end point for fetching task info
]