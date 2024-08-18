from django.db.models.signals import post_save
from django.db.models.signals import post_migrate
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.core.management import call_command


@receiver(post_save, sender=User)
def create_groups_for_new_user(sender, instance, created, **kwargs):
    if created:

        Group.objects.get_or_create(name='Doctor')
        Group.objects.get_or_create(name='Patient')





