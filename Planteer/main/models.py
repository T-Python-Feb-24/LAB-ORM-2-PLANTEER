from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('Fruit','Fruit'),
        ('Vegetable ','Vegetable'),
        ('Herb', 'Herb'),
    ]

    name = models.CharField(max_length=200)
    about = models.TextField()
    user_for= models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_edible = models.BooleanField(default=False)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at}"
    
    
class Comment(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.plant.name}"
