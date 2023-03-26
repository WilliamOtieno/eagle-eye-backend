# Generated by Django 4.0 on 2023-03-26 08:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_tempdata_index_tempdata_is_processed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tempdata',
            name='is_processed',
        ),
        migrations.AddField(
            model_name='picdata',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='picdata',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tempdata',
            name='chunk_id',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempdata',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tempdata',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]