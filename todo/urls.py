from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("add/", views.task_create, name="task_create"),
    path("edit/<int:id>/", views.task_update, name="task_update"),
    path("delete/<int:id>/", views.task_delete, name="task_delete"),
    path("toggle/<int:id>/", views.task_toggle_complete, name="task_toggle_complete"),
]