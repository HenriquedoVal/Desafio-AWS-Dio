# Generated by Django 4.0.3 on 2022-04-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_movies_movie_alter_movie_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='curr_ep',
            field=models.IntegerField(null=True, verbose_name='Current Ep'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='episodes',
            field=models.IntegerField(null=True, verbose_name='Episodes'),
        ),
    ]
