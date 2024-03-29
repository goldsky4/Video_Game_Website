# Generated by Django 2.2 on 2019-05-29 22:55

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_page', '0008_auto_20190529_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='ratingid',
        ),
        migrations.RemoveField(
            model_name='game',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='userid',
        ),
        migrations.CreateModel(
            name='UserGames',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gameid', models.ManyToManyField(to='user_page.Game')),
                ('ratingid', models.ManyToManyField(to='user_page.rating')),
                ('userid', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
