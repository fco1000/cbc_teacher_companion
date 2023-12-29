from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from django.contrib.auth.models import Group

@receiver(post_save, sender=User)
def assign_group_to_user(sender, instance,created,**kwargs):
    if created:
        staff_group = Group.objects.get(name='staff')
        instance.groups.add(staff_group)