# Generated by Django 3.2.5 on 2021-11-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeclStar', '0004_comment_comment_starwidth'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='writer_generation',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer_id',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
