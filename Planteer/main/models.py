from django.db import models
# Create your models here.


class Plant(models.Model):

    #catergories choices
    categories = models.TextChoices("Category", ["Tree", "Fruit", "Vegetable"])

    name = models.CharField(max_length=50)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to='images/')
    category = models.CharField(choices=categories.choices, max_length=12)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=40)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    

