# Generated by Django 4.1.2 on 2022-11-30 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacion',
            name='PerfilAutor',
        ),
    ]
