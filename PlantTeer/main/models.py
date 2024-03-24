from django.db import models

# Create your models here.
class Plant(models.Model):
    
    categories = models.TextChoices("Category", ["Trees", " Shrubs", " Flowering Plants", "Herbaceous Plants"])
    
    name=models.CharField(max_length=2048)
    about=models.TextField()
    used_for=models.TextField()
    image=models.ImageField(upload_to="images/",default="/media/images/succulent-1031033_1280.jpg")
    categroy=models.CharField(max_length=64, choices=categories.choices)
    is_edible=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    
class Contact(models.Model):
    first_name=models.CharField(max_length=2048)
    last_name=models.CharField(max_length=2048)
    email=models.EmailField()
    message=models.TextField
    created_at=models.DateTimeField(auto_now_add=True)
