# Generated by Django 2.2.10 on 2020-06-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]