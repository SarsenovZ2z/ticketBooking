# Generated by Django 2.1.3 on 2018-12-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0006_auto_20181203_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]