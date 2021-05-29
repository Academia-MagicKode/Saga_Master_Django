# Generated by Django 3.1.6 on 2021-03-16 13:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_auto_20210316_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersfollows',
            options={'verbose_name': 'Usuarios Seguidos', 'verbose_name_plural': 'Usuarios Seguidos'},
        ),
        migrations.AddField(
            model_name='post',
            name='stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='users_voted',
            field=models.ManyToManyField(related_name='users_voted', to=settings.AUTH_USER_MODEL, verbose_name='Usuarios que votaron'),
        ),
    ]