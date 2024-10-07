# Generated by Django 5.0.4 on 2024-10-07 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='meeting_string',
            new_name='meeting_summary',
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_recipients',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_transcript',
            field=models.TextField(default=''),
        ),
    ]