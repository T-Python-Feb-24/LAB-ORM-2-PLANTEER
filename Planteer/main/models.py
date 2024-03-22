from django.db import models

# Create your models here.
class Plant(models.Model):
    categories = models.TextChoices("category", ["Tree", "Fruit", "Vegetables"])

    name = models.CharField(max_length=50)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/plant.png")
    category = models.CharField(max_length=64, choices=categories.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)