# Generated by Django 3.0.3 on 2020-08-02 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_image_video_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='platform',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='platform_id',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='result',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]