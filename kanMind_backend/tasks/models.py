from django.db import models
from boards.models import Board
from django.contrib.auth.models import User

STATUS_STATES=(
    ('to-do','To Do'),
    ('in-progress','In Progress'),
    ('review','Review'),
    ('done','Done')
)

PRIORITY_STATES=(
    ('low','Low'),
    ('medium','Medium'),
    ('high','High')
)

class Task(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length = 20 , choices=STATUS_STATES)
    priority = models.CharField(max_length = 20 , choices=PRIORITY_STATES)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_tasks')
    reviewer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='assigned_reviews')
    due_date = models.DateField(editable=True)
    comments_count = models.IntegerField(default=0)
