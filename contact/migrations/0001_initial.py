# Generated by Django 5.0.7 on 2024-07-25 12:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=14)),
                ('dev_type', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Designer', 'Designer')], max_length=9)),
            ],
            options={
                'verbose_name': ('Kontakt ',),
                'verbose_name_plural': 'Kontaktlar',
                'db_table': 'contacts',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backend_dev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backend_groups', to='contact.contact')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designer_groups', to='contact.contact')),
                ('frontend_dev', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frontend_dev_groups', to='contact.contact')),
                ('frontend_dev2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='frontend_dev2_groups', to='contact.contact')),
            ],
        ),
    ]
