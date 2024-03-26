from django.db import models

# Create your models here.



class Plant(models.Model):

    categories = models.TextChoices("Category" , ["Annuals" , "Biennials" , "Perennials" , "Shrub"])
    name = models.CharField(max_length=2048)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/default.jpeg")
    category = models.CharField(max_length=64, choices=categories.choices)
    is_edible = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    

    

class Comment(models.Model):

    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=2084)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.full_name} - {self.plant.name}"
    



class Contact(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
