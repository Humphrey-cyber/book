# Generated by Django 5.1.1 on 2024-09-30 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joseph', '0006_rename_images_homepageimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomepageImage',
            new_name='images',
        ),
    ]
