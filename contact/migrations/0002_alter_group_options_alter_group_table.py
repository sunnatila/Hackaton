# Generated by Django 5.0.7 on 2024-07-25 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': ('Guruh ',), 'verbose_name_plural': 'Guruhlar'},
        ),
        migrations.AlterModelTable(
            name='group',
            table='groups',
        ),
    ]