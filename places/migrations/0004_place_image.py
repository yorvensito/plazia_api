# Generated by Django 5.2.4 on 2025-07-11 16:20

import places.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_place_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=places.utils.place_image_upload_path),
        ),
    ]
