# Generated by Django 2.2 on 2019-05-29 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_page', '0009_auto_20190529_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergames',
            name='ratingid',
        ),
        migrations.AddField(
            model_name='usergames',
            name='user_rating',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='rating',
        ),
    ]
