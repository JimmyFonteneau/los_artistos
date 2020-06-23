# Generated by Django 2.2.10 on 2020-06-23 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0006_auto_20200623_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork_Storage_Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
            ],
            options={
                'verbose_name': "Lieu de stockage de l'oeuvre",
                'verbose_name_plural': 'Lieux de stockage des oeuvres',
            },
        ),
        migrations.AddField(
            model_name='artwork',
            name='storage_place',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='artworks.Artwork_Storage_Place', verbose_name='Lieu de stockage'),
        ),
    ]