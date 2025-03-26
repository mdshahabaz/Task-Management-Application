from django.db import models

'''
User model has the following fields:
    1. User Name
    2. User Email
    3. User Mobile
    4. Created at 
    5. Updated at
'''
class User(models.Model):
    user_name = models.CharField(
        max_length=600,
        default=None,
        null=False,
        blank=False
    )
    user_email_address = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )
    user_mobile_number = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
