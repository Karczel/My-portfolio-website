# Generated by Django 5.1.2 on 2025-01-12 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_skilltag'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilltag',
            name='certificate',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
