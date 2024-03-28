from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = models.ImageField(upload_to="images/", default="/ststic/images/avatar.png")

    def __str__(self) -> str:
        return f"{self.user.username} profile"