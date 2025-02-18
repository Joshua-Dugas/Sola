from django.db import models
from django.contrib.auth.models import User

"""DO NOT FORGET TO REGISTER MODEL IN ADMIN.PY"""

#Table for the user profile that has a 1 to 1 relationship with the user table
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    #This prevents a username from printing as object
    def __str__(self):
        return f"{self.user.username} Profile"

