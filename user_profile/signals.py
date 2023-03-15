from .models import UserProfile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print('sender', sender)
    print('instance', instance)
    print('created', created)
    if created:
        UserProfile.objects.create(user=instance)