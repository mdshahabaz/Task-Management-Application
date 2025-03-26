from django.db import models

# this model defines task status and its choices
class TaskStatus(models.TextChoices):
    UNASSIGNED = "UNASSIGNED","UnAssigned"
    ASSIGNED = "ASSIGNED","Assigned"
    PENDING = "PENDING", "Pending"
    IN_REVIEW = "IN_REVIEW", "In Review"
    QA = "QA", "QA"
    READY_FOR_DEPLOYEMENT = "READY_FOR_DEPLOYEMENT", "Ready for Deployment"
    DONE = "DONE", "Done"
    COMPLETED = "COMPLETED", "Completed"
