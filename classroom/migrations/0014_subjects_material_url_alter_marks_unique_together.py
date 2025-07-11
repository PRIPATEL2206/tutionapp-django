# Generated by Django 5.0.11 on 2025-05-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0013_test_standard'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='material_url',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='marks',
            unique_together={('test', 'student')},
        ),
    ]
