# Generated by Django 3.1.2 on 2020-10-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20201013_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='well',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
