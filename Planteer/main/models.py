from django.db import models

# Create your models here.

class Plant(models.Model):
    
    categories = models.TextChoices()
    
    name = models.CharField(max_length=2000)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_tp ="/images" )
    category = models.CharField(max_length=64,choices= categories.choices)
    is_edible= models.BooleanField()
    created_at = models.DateField(auto_now_add)
    # fix it letter and add (choices + a default image)

# Bonus : 

class Contact(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField()
    messagee = models.TextField()
    created_at = models.DateTimeField(auto_now_add)
    
