# Generated by Django 2.1.3 on 2018-12-07 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_auto_20181204_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(max_length=255, upload_to='')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'poster',
                'verbose_name_plural': 'posters',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.SmallIntegerField()),
                ('col', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'ticket',
                'verbose_name_plural': 'tickets',
            },
        ),
        migrations.AlterModelOptions(
            name='hall',
            options={'verbose_name': 'halll', 'verbose_name_plural': 'halls'},
        ),
        migrations.RenameField(
            model_name='film',
            old_name='poster',
            new_name='main_poster',
        ),
        migrations.AddField(
            model_name='session',
            name='price',
            field=models.CharField(default='1000 KZT', max_length=255),
        ),
        migrations.AddField(
            model_name='ticket',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tickets.Session'),
        ),
        migrations.AddField(
            model_name='poster',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Film'),
        ),
    ]
