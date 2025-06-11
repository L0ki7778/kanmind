from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Task
from authentication.api.serializers import PkToUserInstaceSerializer


class TaskModelSerializer(serializers.ModelSerializer):
    assignee = PkToUserInstaceSerializer(read_only=True)
    reviewer = PkToUserInstaceSerializer(read_only=True)
    assignee_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source=assignee, required=False, write_only=True)
    reviewer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source=reviewer, required=False, write_only=True)

    class Meta:
        model = Task
        fields = [
            'id',
            'board',
            'title',
            'description',
            'status',
            'priority',
            'assignee',
            'reviewer',
            'due_date'
            # 'comments_count'
        ]
