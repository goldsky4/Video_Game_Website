# Generated by Django 2.2 on 2019-05-22 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0002_auto_20190522_1727'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='release_date',
            new_name='first_release_date',
        ),
    ]