# Generated by Django 3.1.6 on 2021-03-20 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20210316_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostOrderingStars',
            fields=[
            ],
            options={
                'ordering': ['-stars'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('posts.post',),
        ),
    ]
