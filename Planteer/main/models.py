from django.db import models


class Plant(models.Model):
    
    categories = models.TextChoices("Category", ["Fruit", "Vegetable", "Flower", "Herb","Tree"])
       

    name = models.CharField(max_length=2048)
    about = models.TextField()
    used_for = models.TextField()
    image = models.ImageField(upload_to="images/", default="images/pexels-photo-1423600.jpeg")
    category = models.CharField(max_length=64, choices=categories.choices)
    is_edible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

class Comment(models.Model):
    
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.full_name} - {self.plant.name}"
