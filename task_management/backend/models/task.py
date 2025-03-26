from django.db import models

from .task_status import TaskStatus
from .task_type import TaskType
from .user import User
from django.utils.timezone import now

'''
Task model has the following fields:
    1. Task name - defines task name
    2. Task Description - defines brief about the task
    3. Task type - defines what type of task it is
    4. Task Assigned to - defines to whom the task is assigned to
    5. Task status - defines if the task is either completed, in review or etc
'''
class Task(models.Model):
    task_name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )
    task_description = models.TextField(
        null=False,
        blank=False
    )
    task_type = models.CharField(
        max_length=100,
        choices=TaskType.choices,
        default=TaskType.TODO
    )
    task_assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="tasks_assigned"
    )
    task_status = models.CharField(
        max_length=100,
        choices=TaskStatus.choices,
        default=TaskStatus.UNASSIGNED
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    completed_at = models.DateTimeField(
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):
        """
        Automatically update `completed_at` when task status changes to `COMPLETED`.
        """
        if self.task_status == TaskStatus.COMPLETED and self.completed_at is None:
            self.completed_at = now()
        elif self.task_status != TaskStatus.COMPLETED:
            self.completed_at = None

        super().save(*args, **kwargs)

