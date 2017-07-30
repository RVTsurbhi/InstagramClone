from django.db import models
from custom_addons.models import BaseModel

# Create your models here.
class UserModel(BaseModel):
      """
       this class is for user profile
      """
      email = models.EmailField(unique=True, null=False, blank=False)
      name = models.CharField(max_length=120)
      username = models.CharField(max_length=120, unique=True, null=False, blank=False)
      password = models.CharField(max_length=120)

class SessionToken(models.Model):
    user = models.ForeignKey(UserModel)
    session_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_session_token(self):
        from uuid import uuid4

        self.session_token = uuid4()

