from django.db import models
from custom_addons.models import BaseModel

# Create your models here.
class UserModel(BaseModel):
      """
       this class is for user profile
      """
      email = models.EmailField(unique=True, null=False, blank=False)
      name = models.CharField(max_length=120)
      username = models.CharField(max_length=120)
      password = models.CharField(max_length=120)

class SessionToken(BaseModel):
    """
     this class is for session token
    """
    user = models.ForeignKey(UserModel)
    session_token = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    is_valid = models.BooleanField(default=True)

    def create_session_token(self):
        from uuid import uuid4

        self.session_token = uuid4()


class PostModel(BaseModel):
    """
     this class is for creating the post
    """
    user = models.ForeignKey(UserModel)
    image = models.FileField(upload_to='user_images')
    image_url = models.CharField(max_length=255)
    caption = models.CharField(max_length=250)

