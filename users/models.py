from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    #def save(self, **kwargs):
    #    super().save()

    #    img = Image.open(self.image.path)
    #    if img.height > 300 or img.width > 300:
    #        output_size = (175,175)
    #        img.thumbnail(output_size)
    #        img.save(self.image.path)



def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)
