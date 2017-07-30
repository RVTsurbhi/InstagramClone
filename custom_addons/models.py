from django.db import models


class BaseModel(models.Model):
    """
     this class is for future references which will be used in almost every model
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True