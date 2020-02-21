from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models. ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    about = RichTextField(blank = True)
    education = models.CharField( max_length = 200, blank=True )
    employment = models.CharField( max_length = 200, blank = True )
    location = models.CharField( max_length = 200, blank = True )


    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            image_size = (300,300)
            img.thumbnail(image_size)
            img.save(self.image.path)        
