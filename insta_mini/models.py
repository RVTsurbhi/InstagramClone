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
    has_liked = False

    #create a function virtually of like count on a post
    @property
    def like_count(self):
        return len(LikeModel.objects.filter(post=self))

    #create a function to return the comments on a current post
    @property
    def comments(self):
        return CommentModel.objects.filter(post=self).order_by('created_on')


class LikeModel(BaseModel):
    """
     this class is for no. of likes (which user like which post)
    """
    user = models.ForeignKey(UserModel)
    post = models.ForeignKey(PostModel)

class CommentModel(BaseModel):
    """
     this class shows the comments
    """
    user = models.ForeignKey(UserModel)
    post = models.ForeignKey(PostModel)
    comment_text = models.CharField(max_length=500)

