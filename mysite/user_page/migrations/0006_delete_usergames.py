# Generated by Django 2.2 on 2019-05-26 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0005_game_userid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserGames',
        ),
    ]
