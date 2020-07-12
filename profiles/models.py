from PIL import Image
from django.db import models
from django.dispatch import receiver
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

from users.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, null=True, blank=True)
    direction = models.CharField(max_length=80, null=True, blank=True)
    image = models.ImageField(default='avatar.png', upload_to='profiles/')
    slug = models.SlugField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def set_profile_user(sender, instance, *args, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def set_image(sender, instance, *args, **kwargs):
    img = Image.open(instance.image.path)
    if img.height > 400 and img.width > 400:
        size = (400, 400)
        img.thumbnail(size)
        img.save(instance.image.path)


@receiver(pre_save, sender=Profile)
def set_slug_profile(sender, instance, *args, **kwargs):
    if instance.user.username:
        instance.slug = slugify(instance.user.username)
