# Generated by Django 5.1.1 on 2024-10-09 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph', '0013_delete_profile_alter_portfolio_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home_images/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
