from django.db import models

# this model defines task and it's types
class TaskType(models.TextChoices):
    TODO = "TODO", "To-Do"
    BUG = "BUG", "Bug"
    FEATURE = "FEATURE", "Feature Request"
    IMPROVEMENT = "IMPROVEMENT", "Improvement"
    CUSTOMIZATION = "CUSTOMIZATION", "Customization"
