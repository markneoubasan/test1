# Generated by Django 5.1.1 on 2025-01-15 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_instructor_verified_credentials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='verified_credentials',
            field=models.ImageField(blank=True, null=True, upload_to='credentials/'),
        ),
    ]
