# Generated by Django 4.0.7 on 2022-10-10 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_rename_idusuario_publicacion_autor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagen',
            old_name='Imagen',
            new_name='imagen',
        ),
    ]