# Generated by Django 5.1.1 on 2024-09-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_game_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(upload_to='static/img'),
        ),
    ]
