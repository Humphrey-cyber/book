# Generated by Django 5.1.1 on 2024-10-08 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph', '0010_delete_images_alter_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
