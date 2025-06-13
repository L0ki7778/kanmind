from django.urls import path
from .views import TaskListCreateView,TaskUpdateDeleteView

urlpatterns = [
    path('', TaskListCreateView.as_view()),
    path('<int:id>/', TaskUpdateDeleteView.as_view(), name='update_task'),
    path('<int:id>/assigned-to-me/', TaskUpdateDeleteView.as_view(), name='assigned_task'),
    path('<int:id>/reviewing/', TaskUpdateDeleteView.as_view(), name='to_review_task'),
]
