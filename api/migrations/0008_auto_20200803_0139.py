# Generated by Django 3.0.3 on 2020-08-02 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200802_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='platform',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='platform_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='result',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
