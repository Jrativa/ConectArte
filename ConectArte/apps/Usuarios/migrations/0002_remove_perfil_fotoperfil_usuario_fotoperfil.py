# Generated by Django 4.1.2 on 2022-11-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='fotoPerfil',
        ),
        migrations.AddField(
            model_name='usuario',
            name='fotoPerfil',
            field=models.ManyToManyField(blank=True, to='Usuarios.imagenperfil'),
        ),
    ]
