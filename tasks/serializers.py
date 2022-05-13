from rest_framework import serializers

from tasks.models import Task


class TasksSerializer(serializers.ModelSerializer):  #Serializer for Task objects
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = ("user", "task_text", "status",)

