# Generated by Django 3.0.3 on 2020-08-03 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200803_0832'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='username',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='username',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
