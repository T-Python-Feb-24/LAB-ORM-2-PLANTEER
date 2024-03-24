from django.db import models
from django.utils import timezone

class Plant(models.Model):
    CATEGORY_CHOICES = [
        ('Fruit','Fruit'),
        ('Vegetable ','Vegetable'),
        ('Herb', 'Herb'),
    ]

    name = models.CharField(max_length=200)
    about = models.TextField()
    user_for= models.TextField()
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    is_edible = models.BooleanField(default=False)
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name