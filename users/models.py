from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # below is how you can resize the image on upload (however its not the most efficient method, google or check the
    # comments on the video for other better methods).

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # First make it do whatever it does normally to save

        img = Image.open(self.image.path)  # Open the image of the current instace

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)  # resize the image
            img.save(self.image.path)  # save the image and replace it to the path of the old image
