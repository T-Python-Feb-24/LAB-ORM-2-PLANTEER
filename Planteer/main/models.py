from django.db import models

# Create your models here.
class Plant(models.Model):

    name =  models.CharField(max_length=200)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default_img.jpg')
    
    Categories = models.TextChoices('Category', ["Tree","Fruit", "Vegetables"]) 
    category = models.CharField(max_length = 64, choices = Categories.choices)

    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)