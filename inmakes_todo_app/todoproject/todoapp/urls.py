from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.add,name = 'add'),
    # path for function based views
    path('delete/<int:task_id>/',views.delete,name = 'delete'),
    path('update/<int:task_id>/',views.update,name = 'update'),
    # path for class based views
    path('cbvhome/',views.TaskListView.as_view(),name = 'cbvhome'),
    path('cbdetail/<int:pk>/',views.TaskDetailView.as_view(),name = 'detail'),
    path('cbupdate/<int:pk>/',views.TaskUpdateView.as_view(),name = 'update'),
    path('cbdelete/<int:pk>/',views.TaskDeleteView.as_view(),name = 'delete')
]
