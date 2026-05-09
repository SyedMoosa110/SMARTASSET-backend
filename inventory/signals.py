from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Assignment, Asset

@receiver(post_save, sender=Assignment)
def update_asset_status(sender, instance, created, **kwargs):
    if created:
        asset = instance.asset
        asset.status = 'Assigned'
        asset.save()
