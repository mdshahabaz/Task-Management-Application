from backend.models.user import User

'''
Service for handling operations related to User class
'''
class UserService:
    # method to create user based on the provided fields.
    def create_user_information(self, user_name, email, mobile_number):
        user_information = User.objects.create(
            user_name=user_name,
            user_email_address=email,
            user_mobile_number=mobile_number
        )
        user_information.save()
    
    # method to get user_id based on the primary key relation. if exists it returns queryset
    def get_user_id(self, user_id):
        return User.objects.filter(id=user_id).exists()