# Generated by Django 4.0 on 2023-03-26 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_tempdata_is_processed_picdata_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='picdata',
            name='is_ready',
            field=models.BooleanField(default=False),
        ),
    ]
