# Generated by Django 5.1.1 on 2024-10-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joseph', '0011_alter_portfolio_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile/')),
            ],
        ),
    ]
