from django.db import models
# Create your models here.

class Plant(models.Model):
    
    categories = models.TextChoices("category",["Tree","Fruits","Vegetables","Grasses","Shrubs","Herbs"])
    
    name = models.CharField(max_length=2000)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to ="images/")
    category = models.CharField(max_length=64,choices = categories.choices)
    is_edible= models.BooleanField()
    created_at = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return self.name
        

class Comment(models.Model):
    plant = models.ForeignKey(Plant,on_delete = models.CASCADE)
    full_name = models.CharField(max_length=2000)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
# Bonus : 

class Contact(models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField()
    messagee = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    

