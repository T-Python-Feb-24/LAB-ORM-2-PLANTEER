from django.db import models

# Create your models here.
class Post(models.Model):
    #catergories choices
    categories = models.TextChoices("Category", ["Fruit", "Tree", "vegetables" ])

    
    Name= models.CharField(max_length=2048)
    about= models.TextField()
    used_for= models.TextField()
    image= models.ImageField(upload_to="images/", default="images/default.jpeg",null=True)
    category= models.CharField(max_length=64, choices=categories.choices,default='General')
    eidble=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    Post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()

def __str__(self):
        return f'Comment by {self.author} on {self.plant.Name}'

