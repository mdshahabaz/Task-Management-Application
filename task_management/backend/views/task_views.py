from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from backend.serializers.task_serializer import AssignTaskSerializer, CreateTaskSerializer
from backend.service.task_service import TaskService



class TaskView(APIView):
    '''Invoking Task Service so that we can use the methods inside of task service whenever needed'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_service_object = TaskService()
    '''
    Based on the URL, we route the requests to correct end points.
    This is done inorder to use multiple HTTP methods in a single APIView.
    '''
    def get(self, request, *args, **kwargs):
        """Differentiate actions based on URL"""
        if request.path.endswith("get-task/"):
            return self.get_task(request)
        else:
            return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        """Differentiate actions based on URL"""
        if request.path.endswith("create/"):
            return self.create_task(request)
        elif request.path.endswith("assign/"):
            return self.assign_task(request)
        else:
            return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)

    # View for getting task related details
    def get_task(self, request):
        user_id = request.query_params.get('user_id')
        if not user_id:
            response = {
                "data":f"No user present in the request body: {user_id}"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        try:
            task_information_object = self.task_service_object.fetch_task_related_info(user_id)
            response = {
                "data":task_information_object
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as error:
            response = {"data":f"Error occured : {error}"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        
    # View for creation of task
    def create_task(self, request):
        serializer = CreateTaskSerializer(data=request.data) # validating incoming data if it is in format of DRF
        if serializer.is_valid(): # if incoming data is not validated, it raises ValidationError with 400 Status Code
            validated_data = serializer.validated_data
            '''The validated data contains data according to the serializers defined, 
            such that no other data enters into the next phase of logic
            '''
            print(validated_data)
            try:
                task_name = validated_data['task_name']
                task_description = validated_data['task_description']
                task_created_by = validated_data['task_created_by']

                task_creation_object = self.task_service_object.\
                    create_task(task_name, task_description,task_created_by)
                print(task_creation_object)
                
                response = {
                    "data":f"Task {task_name} has been created successfully"
                }

                return Response(response, status=status.HTTP_201_CREATED)
            except ValidationError as err:
                response = {"data":f"Validation Error occured: {err}"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            except Exception as error:
                response = {"data":f"Validation Error occured: {error}"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #View for assigning a task to a user
    def assign_task(self, request):
        serializer = AssignTaskSerializer(data=request.data) # validating incoming data if it is in format of DRF
        if serializer.is_valid(): # if incoming data is not validated, it raises ValidationError with 400 Status Code
            validated_data = serializer.validated_data
            '''The validated data contains data according to the serializers defined, 
            such that no other data enters into the next phase of logic
            '''
            print(validated_data)
            try:
                task_id = validated_data['task_id']
                task_assigned_to = validated_data['task_assigned_to']
                task_status = validated_data['task_status']
                task_type = validated_data['task_type']
                task_assigned_by = validated_data['task_assigned_by']

                task_assigning_object = self.task_service_object.\
                    assign_task(task_id,task_type,task_status,task_assigned_to)
                print(task_assigning_object)

                response = {
                    "data":f"Task has been assigned to {task_assigned_to} by {task_assigned_by}"
                }
                return Response(response, status=status.HTTP_201_CREATED)
            except ValidationError as err:
                response = {"data":f"Validation Error occured: {err}"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            except Exception as error:
                response = {"data":f"Validation Error occured: {error}"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # for all other type of serializer errors are caught seperately here.

