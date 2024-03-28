from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Plant(models.Model):
    
    categories = models.TextChoices("Category", ["Tree", "Fruit", "Vegetables" , "Flower"])

    name=models.CharField(max_length = 64)
    about= models.TextField()
    used_for=models.TextField()
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="images/", default="images/default.jpg")
    category=models.CharField(max_length = 64 , choices=categories.choices)



class Contact(models.Model):
    f_name=models.CharField(max_length = 64)
    l_name=models.CharField(max_length = 64)
    email=models.EmailField(max_length=254)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="images/", default="images/user.png")




class Comment(models.Model):
    plant= models.ForeignKey(Plant, on_delete=models.CASCADE)
    name=models.CharField(max_length = 64)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User , on_delete=models.CASCADE)