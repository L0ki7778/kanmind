from datetime import timedelta, date
from django.db import models
from board.models import Board
from django.contrib.auth.models import User

STATUS_STATES = (
    ('to-do', 'To Do'),
    ('in-progress', 'In Progress'),
    ('review', 'Review'),
    ('done', 'Done')
)

PRIORITY_STATES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
)

def one_week_from_now():
    return date.today() + timedelta(weeks=1)
    

class Task(models.Model):
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name="board_task")
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, default='')
    status = models.CharField(choices=STATUS_STATES,
                              default='to-do', max_length=50)
    priority = models.CharField(
        choices=PRIORITY_STATES, default='medium', max_length=10)
    assignee_id = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.SET_NULL, related_name="assigned_tasks")
    reviewer_id = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.SET_NULL, related_name="tasks_to_review")
    due_date = models.DateField(editable=True, default=one_week_from_now)