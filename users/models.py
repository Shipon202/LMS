from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
USER_ROLLES = (
    ('admin', 'Admin'),
    ('teacher', 'Teacher'),
    ('student', 'Student'),
)

class User(AbstractUser):
    role = models.CharField(max_length= 20, choices=USER_ROLLES)
    mobile_no = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return  f"{self.username} ({self.role})"