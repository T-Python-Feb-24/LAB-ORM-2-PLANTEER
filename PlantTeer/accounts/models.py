from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfileUser(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField()
    avatar = models.ImageField(upload_to="images/", default="images/istockphoto-1300845620-612x612.jpg")
    instagram_link = models.URLField(blank=True)
    linked_link = models.URLField(blank=True)

    