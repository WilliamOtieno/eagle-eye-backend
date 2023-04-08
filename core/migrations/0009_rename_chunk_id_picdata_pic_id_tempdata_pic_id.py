# Generated by Django 4.0 on 2023-04-08 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_picdata_images_picdata_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='picdata',
            old_name='chunk_id',
            new_name='pic_id',
        ),
        migrations.AddField(
            model_name='tempdata',
            name='pic_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]