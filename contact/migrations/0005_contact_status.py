# Generated by Django 5.0.7 on 2024-07-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_group_backend_dev_alter_group_designer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
