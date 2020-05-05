from django.urls import path

from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("add",views.addTask,name="add"),
    path("<int:task_id>",views.delete,name="delete")
]