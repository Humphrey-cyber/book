# Generated by Django 5.1.1 on 2024-10-13 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph', '0016_alter_produce_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produce',
            name='image_url',
        ),
        migrations.AddField(
            model_name='produce',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='home_images/'),
        ),
    ]
