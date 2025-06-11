from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Board


class BoardCreateSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), many=True)
    member_count = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ['title', 'members', 'member_count', 'ticket_count',
                  'tasks_to_do_count', 'tasks_high_prio_count','owner_id']
        read_only_fields = ['member_count', 'ticket_count', 'tasks_to_do_count', 'tasks_high_prio_count','owner_id']

    def get_member_count(self, instance):
        return instance.members.count()

    def create(self, validated_data):
        members = validated_data.pop('members', [])
        owner = self.context['request'].user
        board = Board.objects.create(owner = owner,**validated_data)
        board.members.set(members)
        return board
