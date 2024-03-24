from django.db import models

# Create your models here.

class Plants(models.Model):
   categories=models.TextChoices("Category",["Flowers","Trees","Shrubs","Vegetables","Climbing","Herbaceous","Aquatic "])

   name= models.CharField(max_length=2044) 
   about=models.TextField()
   used_for=models.TextField()
   image=models.ImageField(upload_to="images/")
   category=models.CharField(max_length=2055, choices=categories.choices)
   is_edible=models.BooleanField()
   created_at=models.DateTimeField(auto_now_add=True)

class Contact(models.Model):
   first_name=models.CharField(max_length=2000)
   last_name=models.CharField(max_length=2000)
   email=models.EmailField()
   message=models.TextField()
   created_at=models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    plant = models.ForeignKey(Plants, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=2084)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

   
       