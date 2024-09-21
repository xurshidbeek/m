from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from django.contrib.auth.models import User


@receiver(signal=post_save, sender=User)
def print_user_account(sender, instance, created, **kwargs):
    if created:
        email = instance.username + "@gmail.com"
        instance.email = email
        instance.save()


@receiver(signal=pre_delete, sender=User)
def print_deleted_user(sender, instance, **kwargs):
    print(instance.username)
