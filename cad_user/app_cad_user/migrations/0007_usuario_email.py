# Generated by Django 5.0.2 on 2024-02-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_user', '0006_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.TextField(default='', max_length=300),
        ),
    ]
