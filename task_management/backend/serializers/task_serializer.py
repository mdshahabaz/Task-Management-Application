from rest_framework import serializers

from backend.models.task_type import TaskType
from backend.models.task_status import TaskStatus

'''
Serializer helps us in binding data into Python objects and vice-versa
Serializers are also used for validating incoming data
'''
class CreateTaskSerializer(serializers.Serializer):
    task_name = serializers.CharField(
        required=True,
        max_length=255
    )
    task_description = serializers.CharField(
        required=True
    )
    task_created_by = serializers.IntegerField(
        required=True
    )

class AssignTaskSerializer(serializers.Serializer):
    task_id = serializers.IntegerField(
        required=True
    )
    task_status = serializers.CharField(
        required=True
    )
    task_assigned_to = serializers.IntegerField(
        required=True
    )
    task_type = serializers.CharField(
        required=True
    )
    task_assigned_by = serializers.IntegerField(
        required=True
    )