# Generated by Django 4.2.2 on 2023-12-13 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.ImageField(upload_to='article_photos/%y/%m/%d'),
        ),
    ]