# Generated by Django 5.0.6 on 2024-05-17 14:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text2speech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mp3file',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]