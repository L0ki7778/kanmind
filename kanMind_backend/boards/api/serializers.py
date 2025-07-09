from rest_framework import serializers
from ..models import Board
from django.contrib.auth.models import User

class BoardSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, write_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Board
        fields = [
            'id',
            'title',
            'members',
            'member_count',
            'ticket_count',
            'tasks_to_do_count',
            'tasks_high_prio_count',
            'owner_id',
        ]

    def get_member_count(self, instance):
        return instance.members.count()

    def create(self, validated_data):
        members = validated_data.pop("members", [])
        request = self.context.get("request")
        owner = request.user if request else None

        board = Board.objects.create(owner_id=owner, **validated_data)

        board.members.set(members)
        return board

