# Generated by Django 2.2 on 2019-04-24 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NetGuruMovieDB', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 18, 42, 2, 42354), verbose_name='date published'),
        ),
    ]
