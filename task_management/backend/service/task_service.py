from backend.models.task import Task
from backend.models.user import User
from django.core.exceptions import ObjectDoesNotExist

'''
Service layer: Handling database operations and acting as a service layer to the View.
TaskService - Service class for task related operations
'''
class TaskService:

    # method to create a task provided the correct feilds - Perfomrs database operation like creation  
    def create_task(self, task_name, task_description,task_created_by):
        try:
            task_created_by = User.objects.get(id=task_created_by)
            task = Task.objects.create(
                task_name=task_name,
                task_description=task_description,
                created_by=task_created_by
            )
            return task
        
        except ObjectDoesNotExist:
            raise ValueError(f"User with ID {task_created_by} does not exist")
        
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {str(e)}")
        
    # method for assigning a task to a user . Raises valueError if either task or user does not exists  
    def assign_task(self, task_id, task_type, task_status, task_assigned_to):
        try:
            task = Task.objects.get(id=task_id)
            task_assigned_to_user = User.objects.get(id=task_assigned_to)

            task.task_type = task_type
            task.task_status = task_status
            task.task_assigned_to = task_assigned_to_user
            task.save()

            return task

        except Task.DoesNotExist:
            raise ValueError(f"Task with ID {task_id} does not exist")

        except User.DoesNotExist:
            raise ValueError(f"User with ID {task_assigned_to} does not exist")
            
        except Exception as e:
            raise ValueError(f"An unexpected error occurred: {str(e)}")

    # method to fetch task related info provided with user_id. Raises valueError if user_id is not found
    def fetch_task_related_info(self, user_id):
        try:
            task_information = Task.objects.filter(task_assigned_to=user_id).values()
            return task_information
        except ObjectDoesNotExist:
            raise ValueError(f"Task information with ID {user_id} does not exists")
        except Exception as error:
            raise ValueError(f"An unexpected error occured: {str(error)}")
