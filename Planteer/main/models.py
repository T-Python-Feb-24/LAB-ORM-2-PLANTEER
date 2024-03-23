# from django.db import models

# # Create your models here.


# class Post(models.Model):

#     #catergories choices
#     categories = models.TextChoices("Category", ["General", "Tech", "Science", "Fashion"])

#     title = models.CharField(max_length=2048)
#     content = models.TextField()
#     is_published = models.BooleanField()
#     published_at = models.DateTimeField(auto_now_add=True)
#     poster = models.ImageField(upload_to="images/", default="images/default.jpeg")
#     category = models.CharField(max_length=64, choices=categories.choices)
     
# # الادمن
# def __str__(self):
#     return self.title     

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