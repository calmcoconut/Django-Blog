"""signal that fires when a user is created"""

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# we want a user profile to made with each registration

# recieves signal when the user is saves
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwards):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwards):
    instance.profile.save()