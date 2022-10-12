# Generated by Django 4.0.7 on 2022-10-08 22:59

import apps.publicaciones.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imagen', models.ImageField(blank=True, null=True, upload_to=apps.publicaciones.models.user_directory_path)),
            ],
        ),
        migrations.AddField(
            model_name='comentarios',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='comment_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentarios',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='FechaComment',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='comentarios',
            name='IdUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_comentario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='FechaPublicacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='IdUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='autor_publucacion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='Multimedia',
        ),
        migrations.AddField(
            model_name='publicacion',
            name='Multimedia',
            field=models.ManyToManyField(blank=True, to='publicaciones.imagen'),
        ),
    ]