from rest_framework import serializers
from ..models import Board
from tasks.api.seriralizers import TaskListCreateSerializer
from django.contrib.auth.models import User
from authentication.api.serializers import SimpleUserSerializer

class MembersField(serializers.Field):
    
    def to_representation(self, value:User):
        return SimpleUserSerializer(value.all(), many=True).data
    
    def to_internal_value(self, data):
        users=[]
        for pk in data:
            try:
                
                user = User.objects.get(pk=pk)
                users.append(user)
            except User.DoesNotExist:
                raise serializers.ValidationError(f"Ein oder meherere User nicht vorhanden")
        return users
    

class BoardSerializer(serializers.ModelSerializer):
    member_count = serializers.SerializerMethodField()
    members = MembersField()
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

        board = Board.objects.create(owner=owner, **validated_data)

        board.members.set(members)
        return board
    
class SingleBoardSerializer(BoardSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        model = Board
        fields = [
            'id',
            'title',
            'owner_id',
            'members',
            'tasks'
        ]
        
    def get_tasks(self, instance):
        serializer = TaskListCreateSerializer(instance.tasks.all(), many=True)
        if serializer.is_valid():
            return serializer.data
        # return TaskListCreateSerializer(instance.tasks.all(), many=True).data

