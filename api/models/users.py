from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    username = models.CharField(max_length = 100, unique = True, blank = False)
    first_name = models.CharField(max_length = 40, blank = False)
    middle_name = models.CharField(max_length = 40, blank = True)
    last_name = models.CharField(max_length = 40, blank = False)
    email = models.EmailField(unique = True, blank = False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]
    
