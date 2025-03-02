# Generated by Django 5.1.1 on 2025-01-15 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_enrollment_completion_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='completion_status',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='enrollment_status',
            field=models.CharField(choices=[('Pending', 'pending'), ('Approved', 'approved'), ('Disapproved', 'disapproved')], default='', max_length=11),
        ),
    ]
