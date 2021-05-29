from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    is_banned=models.BooleanField(default=False)
    post_number=models.IntegerField(default=0)

    @property
    def posts(self):
        return self.post_set.all()

    def __str__(self):
        return self.username