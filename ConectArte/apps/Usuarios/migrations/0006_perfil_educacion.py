# Generated by Django 4.0.7 on 2022-10-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_alter_perfil_descripcion_alter_perfil_experiencia_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='Educacion',
            field=models.TextField(default='', null=True, verbose_name='Educacion'),
        ),
    ]
