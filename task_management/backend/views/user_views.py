from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from backend.models.user import User
from backend.service.user_service import UserService
from backend.serializers.user_serializer import UserCreateSerializer

'''UserView API. Deals with Creation of User data'''
class UserView(APIView):
    '''Invoking UserService class such that the methods inside of the class can be used whenever needed.'''
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()
    
    # View for creation of user
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data) # validating incoming data if it is in format of DRF
        serializer.is_valid(raise_exception=True) # if incoming data is not validated, it raises ValidationError with 400 Status Code
        validated_data = serializer.validated_data
        ''' The validated data contains data according to the serializers defined, 
            such that no other data enters into the next phase of logic
        '''
        print(validated_data)
        try:
            user_name = validated_data['user_name']
            user_email = validated_data['user_email_address']
            user_mobile = validated_data['user_mobile_number']

            user_response = self.user_service.\
                create_user_information(user_name,user_email,user_mobile)
            response = {
                "data" : f"User {user_response.user_name} has been created successfully"
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except ValidationError as err:
            response = {
                "data":f"Validation Error occured: {err}"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            response = {
                "data":f"Error occured while creating user: {error.detail}"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

