# Generated by Django 5.1.1 on 2024-10-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph', '0007_rename_homepageimage_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomepageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='homepage_images/')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
