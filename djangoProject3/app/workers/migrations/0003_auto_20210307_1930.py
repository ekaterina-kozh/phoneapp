# Generated by Django 3.1.7 on 2021-03-07 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_auto_20210307_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
