# Generated by Django 3.1.6 on 2021-03-20 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_post_numbre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='post_numbre',
            new_name='post_number',
        ),
    ]