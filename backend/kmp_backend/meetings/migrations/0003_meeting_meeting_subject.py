# Generated by Django 5.0.4 on 2024-10-07 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_rename_meeting_string_meeting_meeting_summary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_subject',
            field=models.TextField(default=''),
        ),
    ]
