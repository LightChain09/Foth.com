from django.db import models
import django.contrib.auth.models as auth_models

class Profile(models.Model):
    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE)
    steam_id = models.CharField(max_length=18, default="")


    def __str__(self):
        return f"{self.user.username} Profile"