# Generated by Django 2.1.3 on 2018-12-07 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_auto_20181207_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_at',
            field=models.DateTimeField(),
        ),
    ]