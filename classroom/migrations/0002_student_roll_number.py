# Generated by Django 5.0.11 on 2025-04-23 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='roll_number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
