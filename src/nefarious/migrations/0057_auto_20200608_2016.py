# Generated by Django 3.0.2 on 2020-06-08 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nefarious', '0056_watchtvseasonrequest_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchmovie',
            name='download_path',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='watchtvepisode',
            name='download_path',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='watchtvseason',
            name='download_path',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
