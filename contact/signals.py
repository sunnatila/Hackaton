from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Contact, Group


@receiver(post_delete, sender=Contact)
def cleanup_on_contact_delete(sender, instance, **kwargs):
    Group.objects.filter(backend_dev=instance).update(backend_dev=None)
    Group.objects.filter(frontend_dev=instance).update(frontend_dev=None)
    Group.objects.filter(frontend_dev2=instance).update(frontend_dev2=None)
    Group.objects.filter(designer=instance).update(designer=None)

    # To'liq bo'sh guruhlarni o'chirish
    for group in Group.objects.all():
        if not any([group.backend_dev, group.frontend_dev, group.frontend_dev2, group.designer]):
            group.delete()
