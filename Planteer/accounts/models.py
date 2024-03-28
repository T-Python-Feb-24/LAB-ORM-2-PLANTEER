from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = models.ImageField(upload_to="images/", default="images/user.png")
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)


    def __str__(self) -> str:
        return f"{self.user.username} profile"