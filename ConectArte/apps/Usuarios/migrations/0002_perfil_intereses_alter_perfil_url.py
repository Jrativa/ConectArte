# Generated by Django 4.0.7 on 2022-10-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='Intereses',
            field=models.TextField(default='', verbose_name='Intereses'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='url',
            field=models.CharField(max_length=30),
        ),
    ]
