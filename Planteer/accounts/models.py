from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin_link=models.URLField(blank=True)
    avatar=models.ImageField(upload_to="images/", default="/static/images/ava.png")
    
    def __str__(self) -> str:
        return f"{self.user.username} profile"