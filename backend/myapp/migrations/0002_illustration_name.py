# Generated by Django 5.1.2 on 2025-01-10 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='illustration',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
