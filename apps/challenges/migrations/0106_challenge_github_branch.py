# Generated by Django 2.2.20 on 2023-08-23 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0105_challenge_sponsors_prizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='github_branch',
            field=models.CharField(blank=True, default='challenge', max_length=200, null=True),
        ),
    ]
