# Generated by Django 5.0.2 on 2024-02-08 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_user', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]