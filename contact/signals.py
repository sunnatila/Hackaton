from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.db import connection, transaction
from .models import Contact, Group


@receiver(post_delete, sender=Contact)
def reset_contact_id(sender, instance, **kwargs):
    with connection.cursor() as cursor:
        # Contact jadvalidan barcha yozuvlarni o'chirish
        cursor.execute("DELETE FROM contacts;")
        # sqlite_sequence jadvalini yangilash
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='contacts';")

    # Django'da atomic blokdan tashqarida tranzaksiya
    try:
        with transaction.atomic():
            # Atomic blokni tugatib, VACUUM'ni alohida bajaring
            connection.cursor().execute("VACUUM;")
    except Exception as e:
        # Tranzaksiyada xatolik yuz berdi
        print(f"Error: {e}")


@receiver(post_delete, sender=Group)
def reset_group_id(sender, instance, **kwargs):
    with connection.cursor() as cursor:
        # Group jadvalidan barcha yozuvlarni o'chirish
        cursor.execute("DELETE FROM groups;")
        # sqlite_sequence jadvalini yangilash
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='groups';")

    # Django'da atomic blokdan tashqarida tranzaksiya
    try:
        with transaction.atomic():
            # Atomic blokni tugatib, VACUUM'ni alohida bajaring
            connection.cursor().execute("VACUUM;")
    except Exception as e:
        # Tranzaksiyada xatolik yuz berdi
        print(f"Error: {e}")

