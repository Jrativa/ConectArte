# Generated by Django 4.0.7 on 2022-10-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_rename_descripción_perfil_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='Descripcion',
            field=models.TextField(default='', null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Experiencia',
            field=models.TextField(default='', null=True, verbose_name='Experiencia'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='Intereses',
            field=models.TextField(default='', null=True, verbose_name='Intereses'),
        ),
    ]