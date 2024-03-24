from django.db import models

# Create your models here.
class Post(models.Model):
    #catergories choices
    categories = models.TextChoices("Category", ["General", "Tech", "Science", "Fashion"])

    
    Name= models.CharField(max_length=2048)
    about= models.TextField()
    used_for= models.TextField()
    image= models.ImageField(upload_to="images/", default="images/default.jpeg",null=True)
    category= models.CharField(max_length=64, choices=categories.choices,default='General')
    eidble=models.BooleanField(default=True)


