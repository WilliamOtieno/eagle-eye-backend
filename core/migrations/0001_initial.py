# Generated by Django 4.1.7 on 2023-03-26 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PicData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chunk_id', models.CharField(max_length=256)),
                ('chip', models.CharField(max_length=256)),
                ('vision', models.TextField()),
                ('length', models.BigIntegerField(default=0)),
                ('batt', models.IntegerField(default=0)),
                ('is_full', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='pics/')),
            ],
        ),
    ]