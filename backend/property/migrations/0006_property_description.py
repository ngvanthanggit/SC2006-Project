# Generated by Django 5.1.7 on 2025-04-08 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_remove_property_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
