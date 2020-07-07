# Generated by Django 2.2.10 on 2020-07-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_merge_20200701_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'En attente'), (2, 'Confirmée'), (3, 'Refusée')], default=2),
        ),
    ]