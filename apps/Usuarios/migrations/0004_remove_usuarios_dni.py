# Generated by Django 4.2.3 on 2023-07-16 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_alter_usuarios_fecha_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='dni',
        ),
    ]