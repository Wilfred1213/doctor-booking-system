from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length = 255, null = True, blank = True)
    fullname = models.CharField(max_length = 255, null = True, blank = True) 
    image = models.ImageField(upload_to='user_images', null = True)
    is_doctor = models.BooleanField('Are you a Doctor?', default=False, null = True, blank = True)
    
    def __str__(self):
        return self.username
