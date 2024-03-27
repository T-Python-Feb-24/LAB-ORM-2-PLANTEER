from django.db import models
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True


def group_based_upload_to(instance, filename):
   return "image/{}/{}".format(instance.user.id, filename)


class Profile(models.Model):
   class nationality_choices(models.TextChoices):
      SA = "Saudi Arabia"
      UAE = "United Arab Emirates"

   user = models.OneToOneField(User, on_delete=models.CASCADE)
   about = models.TextField()
   avatar = models.ImageField(
       upload_to=group_based_upload_to, default="images/profiles/user-defualt.svg")
   nationality = models.CharField(max_length=20,
                                  choices=nationality_choices.choices,
                                  default=nationality_choices.SA)

   def __str__(self) -> str:
      return f"{self.user.username} profile"
