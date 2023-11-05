from django.db import models
from users.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images')

    def __str__(self):
        return self.user.username
    
