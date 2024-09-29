# Generated by Django 5.1.1 on 2024-09-25 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_game_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='User',
        ),
        migrations.RemoveField(
            model_name='game',
            name='age_limited',
        ),
        migrations.AddField(
            model_name='game',
            name='reviews',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
