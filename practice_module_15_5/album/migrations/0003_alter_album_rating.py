# Generated by Django 4.2.4 on 2024-05-31 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_alter_album_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1),
        ),
    ]
