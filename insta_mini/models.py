from django.db import models
from custom_addons.models import BaseModel

# Create your models here.
class UserModel(BaseModel):
      """
       this class is for user profile
      """
      email = models.EmailField()
      name = models.CharField(max_length=120)
      username = models.CharField(max_length=120)
      password = models.CharField(max_length=40)
