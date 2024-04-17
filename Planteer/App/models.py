from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    #catergories choices
    categories = models.TextChoices("Category", ["Fruit", "Tree", "vegetables" ])

    
    Name= models.CharField(max_length=2048)
    about= models.TextField()
    used_for= models.TextField()
    image= models.ImageField(upload_to="images/", default="images/0001.jpg",null=True)
    category= models.CharField(max_length=64, choices=categories.choices,default='General')
    eidble=models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now())


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())



class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.full_name
