# Generated by Django 4.2.1 on 2023-05-21 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodhouse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='item_images'),
        ),
    ]
