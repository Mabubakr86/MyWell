# Generated by Django 3.1.2 on 2020-10-13 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_well_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Workover', 'Workover'), ('Troubleshooting', 'Troubleshooting'), ('Optimization', 'Optimization'), ('Other', 'Other')], max_length=200),
        ),
    ]
