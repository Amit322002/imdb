# Generated by Django 5.1 on 2024-09-24 09:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imdb_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='platform',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='imdb_api.streamplatform'),
        ),
    ]
