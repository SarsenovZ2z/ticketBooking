# Generated by Django 2.1.3 on 2018-12-08 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0012_auto_20181207_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='main_poster',
            field=models.ImageField(upload_to='films'),
        ),
        migrations.AlterField(
            model_name='poster',
            name='image',
            field=models.ImageField(upload_to='posters'),
        ),
    ]
