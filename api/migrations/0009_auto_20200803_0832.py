# Generated by Django 3.0.3 on 2020-08-03 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200803_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='abuser',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='complainer',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='victim',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
