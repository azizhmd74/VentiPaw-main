# Generated by Django 4.2.2 on 2024-05-18 16:51

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_alter_article_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='article image'),
        ),
    ]
