# Generated by Django 3.2.5 on 2021-11-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeclBoard', '0002_board_writer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_board',
            name='comment_writer',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
