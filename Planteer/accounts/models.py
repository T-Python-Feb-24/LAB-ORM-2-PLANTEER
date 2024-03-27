from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = models.ImageField(upload_to="images/", default="images/avatar.webp")
    instagram_link = models.URLField(blank=True)
    linked_link = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} profile"