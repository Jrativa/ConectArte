# Generated by Django 4.0.7 on 2022-11-29 03:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Usuarios', '0001_initial'),
        ('DM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='canalusuario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='canalmensaje',
            name='canal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DM.canal'),
        ),
        migrations.AddField(
            model_name='canalmensaje',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='canal',
            name='usuarios',
            field=models.ManyToManyField(blank=True, through='DM.CanalUsuario', to=settings.AUTH_USER_MODEL),
        ),
    ]