from unittest.util import _MAX_LENGTH
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from sorl.thumbnail import ImageField


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE, # Will delete profile if user is deleted
        related_name="profile"
    )
    image = ImageField(upload_to="profiles")
    bio = models.CharField(max_length=140, blank=False, null=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a new Profile() object when a Django user is created."""
    if created:
        Profile.objects.create(user=instance)