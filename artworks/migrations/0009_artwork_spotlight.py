# Generated by Django 2.2.10 on 2020-06-23 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0008_artwork_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='spotlight',
            field=models.BooleanField(default=False, verbose_name='Mise en avant'),
        ),
    ]
