# Generated by Django 4.2.3 on 2023-07-16 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_remove_usuarios_dni'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='imagen',
            field=models.ImageField(blank=True, default='usuarios/usuario_def.png', null=True, upload_to='usuarios'),
        ),
    ]