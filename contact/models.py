from django.db import models
from rest_framework.exceptions import ValidationError


class Contact(models.Model):
    DEVELOPER_TYPE = (
        ('Frontend', 'Frontend'),
        ('Backend', 'Backend'),
        ('Designer', 'Designer')
    )

    fullname = models.CharField(max_length=100)
    phone = models.CharField(max_length=14)
    dev_type = models.CharField(max_length=9, choices=DEVELOPER_TYPE)
    status = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'Kontakt '
        verbose_name_plural = 'Kontaktlar'
        db_table = 'contacts'


class Group(models.Model):
    backend_dev = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='backend_groups',
        null=True,
        blank=True
    )
    frontend_dev = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='frontend_dev_groups',
        null=True,
        blank=True
    )
    frontend_dev2 = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='frontend_dev2_groups',
        null=True,
        blank=True
    )
    designer = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name='designer_groups',
        null=True,
        blank=True
    )

    objects = models.Manager()

    def __str__(self):
        return f'{str(self.id)} - guruh'

    def save(self, *args, **kwargs):
        if Group.objects.count() >= 6 and not self.pk:
            raise ValidationError("Only 6 groups can be created.")
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Guruhlar'
        verbose_name = 'Guruh '

        db_table = 'groups'
