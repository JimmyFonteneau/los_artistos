# Generated by Django 2.2.10 on 2020-08-08 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
            ],
            options={
                'verbose_name': "Catégorie de l'oeuvre",
                'verbose_name_plural': 'Catégories des oeuvres',
            },
        ),
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
        migrations.CreateModel(
            name='Artwork_Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
            ],
            options={
                'verbose_name': "Style de l'oeuvre",
                'verbose_name_plural': 'Style des oeuvres',
            },
        ),
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Non loué'), (2, 'Loué')], default=1, null=True)),
                ('name', models.CharField(max_length=200, verbose_name='Nom')),
                ('height', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Hauteur (cm)')),
                ('width', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Largeur (cm)')),
                ('price', models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Prix (€)')),
                ('spotlight', models.BooleanField(default=False, verbose_name='Mise en avant')),
                ('photo', models.ImageField(default='/default.jpg', upload_to='artworks')),
                ('timer', models.DateField(blank=True, null=True, verbose_name='Timer')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artists.Artist', verbose_name='Artiste')),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='artworks.Artwork_Category', verbose_name='Catégorie')),
                ('storage_place', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='artworks.Artwork_Storage_Place', verbose_name='Lieu de stockage')),
                ('style', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='artworks.Artwork_Style', verbose_name='Style')),
            ],
            options={
                'verbose_name': 'Oeuvre',
                'verbose_name_plural': 'Oeuvres',
            },
        ),
    ]