from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Task
from authentication.api.serializers import SimpleUserSerializer


class TaskListCreateSerializer(serializers.ModelSerializer):
    # Serializer get's used to display the needed data only
    assignee = SimpleUserSerializer(read_only=True)
    reviewer = SimpleUserSerializer(read_only=True)
    assignee_id = serializers.PrimaryKeyRelatedField(  # need id for corresponding model-relation (PK) and disable required to allow Null
        queryset=User.objects.all(), source='assignee', write_only=True, required=False)
    reviewer_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='reviewer', write_only=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'priority',
                  'comments_count', 'board', 'assignee', 'reviewer', 'assignee_id',
                  'reviewer_id','due_date']


# class TaskDetailSerializer(serializers.ModelSerializer):
