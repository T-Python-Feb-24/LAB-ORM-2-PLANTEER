from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django.contrib.auth.models import User

class Plant(models.Model):

    categories = models.TextChoices("Category", ["Tree",  "Fruit", "Vegetables"])
    
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_edible = models.BooleanField()
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to="images/", default="images/def.jpg")
    category = models.CharField(max_length=30, choices=categories.choices)

    def __str__(self) -> str:
        return self.title
    
class Contact(models.Model):

    first_name = models.CharField(max_length=2048)
    last_name = models.CharField(max_length=2048)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.plant.title}"