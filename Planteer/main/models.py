from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plant(models.Model):
    categories=models.TextChoices("categore",["General","Flowering","Conifers","Mosses","Carnivorous"])
    name=models.CharField(max_length=2048)
    about=models.TextField()
    used_for=models.TextField()
    image=models.ImageField(upload_to="images/", default="images/plants3_D7jRXh6.png")
    categore=models.CharField(max_length=64, choices=categories.choices)
    is_edible=models.BooleanField()
    created_at=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class Contact(models.Model):
    first_name = models.CharField(max_length=2048)
    last_name = models.CharField(max_length=2048)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name
    

class Comment(models.Model):
    plant= models.ForeignKey(Plant, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.plant.name}"


