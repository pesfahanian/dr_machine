import os
from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser

from backend.settings.base import MEDIA_ROOT


@receiver(post_save, sender=CustomUser)
def create_user(sender, instance, created, **kwargs):
    if created:
        now = str(datetime.now()).split(' ')[0]
        directory_name = f'{now}_{str(instance.nickname)}'
        directory_path = os.path.join(MEDIA_ROOT, directory_name)
        print(directory_path)
        os.makedirs(directory_path)
